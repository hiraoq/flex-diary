import React from 'react';
import { Routes, Route } from 'react-router-dom';
import DiaryForm from './features/diary/DiaryForm';
import DiaryList from './features/diary/DiaryList';
import { Container, Typography, Card, CardContent } from '@mui/material';

const App = () => {
  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Flex Diary UI
      </Typography>
      <Routes>
        <Route
          path="/"
          element={
            <>
              <Card style={{ marginBottom: '16px' }}>
                <CardContent>
                  <DiaryForm />
                </CardContent>
              </Card>
              <Card>
                <CardContent>
                  <DiaryList />
                </CardContent>
              </Card>
            </>
          }
        />
        <Route path="/diary/:id" element={<DiaryForm />} />
      </Routes>
    </Container>
  );
};

export default App;
