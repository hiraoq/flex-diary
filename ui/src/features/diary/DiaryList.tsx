import type React from 'react';
import { useState, useEffect } from 'react';
import { fetchDiaries, selectDiaries } from './diarySlice';
import {
  List, ListItem, ListItemText, Pagination, Typography, Card, CardContent, TextField,
} from '@mui/material';
import { useAppDispatch, useAppSelector } from '../../app/hooks';
import { LocalizationProvider, DatePicker } from '@mui/x-date-pickers';
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFnsV3';

const DiaryList = () => {
  const dispatch = useAppDispatch();
  const diaries = useAppSelector(selectDiaries);
  const [month, setMonth] = useState(new Date().getMonth() + 1);
  const [year, setYear] = useState(new Date().getFullYear());

  useEffect(() => {
    dispatch(fetchDiaries(month));
  }, [month, dispatch]);

  const handleMonthChange = (event: React.ChangeEvent<unknown>, value: number) => {
    setMonth(value);
  };

  const handleYearChange = (date: Date | null) => {
    if (date) {
      setYear(date.getFullYear());
    }
  };

  return (
    <div>
      <Typography variant="h6">Diary Entries</Typography>
      <Pagination
        count={12}
        page={month}
        onChange={handleMonthChange}
      />
      <List>
        {diaries.map((diary) => (
          <ListItem button key={diary.id} component="a" href={`/diary/${diary.id}`}>
            <ListItemText
              primary={diary.title}
              secondary={
                <>
                  {diary.date}
                  <br />
                  {diary.body}
                </>
              }
            />
          </ListItem>
        ))}
      </List>
      <LocalizationProvider dateAdapter={AdapterDateFns}>
        <DatePicker
          views={['year']}
          label="Year"
          value={new Date(year, 0)}
          onChange={handleYearChange}
          slotProps={{ textField: { variant: 'outlined' } }}
        />
      </LocalizationProvider>
    </div>
  );
};

export default DiaryList;
