import React from 'react';
import { useForm } from 'react-hook-form';
import { useParams, useNavigate } from 'react-router-dom';
import { fetchDiary, updateDiary, selectDiaryById } from './diarySlice';
import { TextField, Button, Typography } from '@mui/material';
import { useAppDispatch, useAppSelector } from '../../app/hooks';

type DiaryFormData = {
  title: string;
  body: string;
};

const DiaryForm = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const dispatch = useAppDispatch();
  const diary = useAppSelector((state) => selectDiaryById(state, id || ''));
  const { register, handleSubmit, setValue } = useForm<DiaryFormData>();

  React.useEffect(() => {
    if (id) {
      dispatch(fetchDiary(id));
    }
  }, [id, dispatch]);

  React.useEffect(() => {
    if (diary) {
      setValue('title', diary.title);
      setValue('body', diary.body);
    }
  }, [diary, setValue]);

  const onSubmit = (data: DiaryFormData) => {
    if (id && diary) {
      const updatedDiary = { id, ...data, date: diary.date };
      console.log('Updated Diary:', updatedDiary); // コンソールに結果を表示
      // dispatch(updateDiary(updatedDiary)); // 実際のAPI呼び出しをコメントアウト
      alert('Diary updated!'); // アラートを表示
      navigate(`/diary/${id}`);
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <Typography variant="h6">New Diary Entry</Typography>
      <TextField {...register('title')} label="Title" fullWidth margin="normal" />
      <TextField {...register('body')} label="Body" multiline rows={4} fullWidth margin="normal" />
      <Button type="submit" variant="contained" color="primary">
        Save
      </Button>
    </form>
  );
};

export default DiaryForm;
