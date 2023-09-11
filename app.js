const express = require('express');
const app = express();

// Define a route to handle GET requests with query parameters
app.get('/api', (req, res) => {
  // Retrieve and validate query parameters
  const slackName = req.query.slack_name;
  const track = req.query.track;

  if (!slackName || !track) {
    return res.status(400).json({ error: 'Both slack_name and track are required' });
  }

  // Get the current day of the week in full
  const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  const currentDay = daysOfWeek[new Date().getDay()];

  // Get the current UTC time with +/-2 minute window
  const currentUtcTime = new Date().toISOString();

  // Define GitHub URLs (Replace with actual URLs)
  const githubFileUrl = 'https://github.com/adannalyn/hngx/blob/main/appy.py';
  const githubRepoUrl = 'https://github.com/adannalyn/hngx.git';

  // Construct the JSON response
  const responseJson = {
    slack_name: slackName,
    current_day: currentDay,
    utc_time: currentUtcTime,
    track: track,
    github_file_url: githubFileUrl,
    github_repo_url: githubRepoUrl,
    status_code: 200 // Success status code
  };

  // Send the JSON response
  res.json(responseJson);
});

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
