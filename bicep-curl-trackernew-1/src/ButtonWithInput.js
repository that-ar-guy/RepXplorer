import React, { useState, useEffect } from "react";
import { Button, TextField, Typography } from "@material-ui/core";
import io from "socket.io-client";

const ExerciseComponent = () => {
  const [exerciseInput, setExerciseInput] = useState("");
  const [showInput, setShowInput] = useState(false);
  const [remainingSquats, setRemainingSquats] = useState(10); // Set an initial value
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    // Connect to the socket server
    const socket = io.connect("https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"); // Replace with your actual socket server URL
    setSocket(socket);

    // Cleanup function
    return () => {
      // Disconnect socket when the component unmounts
      socket.disconnect();
    };
  }, []); // Empty dependency array ensures useEffect runs once

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(`Submitted Exercise Input: ${exerciseInput}`);

    // Emit a socket event to update the server with the count
    if (socket) {
      socket.emit("updateSquatCount", { remainingSquats });
    }

    // Add your logic here to handle the submission
  };

  const handleButtonClick = (exerciseType) => {
    setExerciseInput(""); // Reset input when switching exercises
    setShowInput(true);
  };

  return (
    <div className="mt-1 mb-6" style={{ marginRight: "20%" }}>
      <Typography variant="h1" gutterBottom>
        Get Started!
      </Typography>
      <Button
        variant="contained"
        color="primary"
        onClick={() => handleButtonClick("Squats")}
      >
        Squats
      </Button>
      <Button
        variant="contained"
        color="primary"
        onClick={() => handleButtonClick("Bicep Curls")}
        style={{ marginLeft: "10px" }}
      >
        Bicep Curls
      </Button>
      {showInput && (
        <form onSubmit={handleSubmit} className="mt-2">
          <TextField
            fullWidth
            margin="normal"
            label={`Number of Reps for ${exerciseInput}`}
            type="number"
            variant="outlined"
            value={exerciseInput}
            onChange={(e) => setExerciseInput(e.target.value)}
          />
          <Button
            type="submit"
            variant="contained"
            color="white"
            style={{ marginTop: "10px" }}
          >
            Submit
          </Button>
        </form>
      )}
    </div>
  );
};

export default ExerciseComponent;
