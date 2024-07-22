import type { PayloadAction } from '@reduxjs/toolkit';
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import type { RootState } from '../../app/store';

interface Diary {
  id: string;
  title: string;
  body: string;
  date: string;
}

interface DiaryState {
  diaries: Diary[];
  diary: Diary | null;
}

const initialState: DiaryState = {
  diaries: [
    { id: '1', title: 'Test Diary 1', body: 'This is a test diary entry 1.', date: '2023-07-01' },
    { id: '2', title: 'Test Diary 2', body: 'This is a test diary entry 2.', date: '2023-07-02' },
    { id: '3', title: 'Test Diary 3', body: 'This is a test diary entry 3.', date: '2023-07-03' },
  ],
  diary: null,
};

export const fetchDiaries = createAsyncThunk<Diary[], number>(
  'diaries/fetchDiaries',
  async (month: number) => {
    // モックデータを返す
    return initialState.diaries.filter((diary) => new Date(diary.date).getMonth() + 1 === month);
  }
);

export const fetchDiary = createAsyncThunk<Diary, string>(
  'diaries/fetchDiary',
  async (id: string) => {
    // モックデータを返す
    return initialState.diaries.find((diary) => diary.id === id)!;
  }
);

export const updateDiary = createAsyncThunk<Diary, Diary>(
  'diaries/updateDiary',
  async (diary) => {
    // 実際のAPI呼び出しはここに書く
    return diary;
  }
);

const diarySlice = createSlice({
  name: 'diaries',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder.addCase(fetchDiaries.fulfilled, (state, action: PayloadAction<Diary[]>) => {
      state.diaries = action.payload;
    });
    builder.addCase(fetchDiary.fulfilled, (state, action: PayloadAction<Diary>) => {
      state.diary = action.payload;
    });
    builder.addCase(updateDiary.fulfilled, (state, action: PayloadAction<Diary>) => {
      const index = state.diaries.findIndex((d) => d.id === action.payload.id);
      if (index !== -1) {
        state.diaries[index] = action.payload;
      }
    });
  },
});

export const selectDiaries = (state: RootState) => state.diaries.diaries;
export const selectDiaryById = (state: RootState, id: string) =>
  state.diaries.diaries.find((diary) => diary.id === id);

export default diarySlice.reducer;
