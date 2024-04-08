<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>ISS Tracker and Notifier</h1>
    <p>The ISS Tracker and Notifier is a Python script that tracks the International Space Station (ISS) and sends email notifications if it's close to the user's current location and if it's currently night time.</p>

  <h2>Features</h2>
    <ul>
        <li><strong>ISS Tracking:</strong> Utilizes the Open Notify API to retrieve the current latitude and longitude of the ISS.</li>
        <li><strong>Location Check:</strong> Determines if the ISS is close to the user's current position by comparing latitudes and longitudes.</li>
        <li><strong>Time Check:</strong> Checks if it's currently night time at the user's location using the Sunrise-Sunset API.</li>
        <li><strong>Email Notification:</strong> Sends an email notification if the ISS is close and it's night time.</li>
        <li><strong>Automated Execution:</strong> The script runs continuously, checking every 60 seconds for the ISS position and night time.</li>
    </ul>

  <h2>Requirements</h2>
    <ul>
        <li>Python</li>
        <li>Requests library</li>
        <li>SMTPlib library</li>
    </ul>

  <h2>Setup</h2>
    <ul>
        <li><strong>Email Configuration:</strong> Provide your email address and password for sending notifications.</li>
        <li><strong>Latitude and Longitude:</strong> Update the latitude and longitude values for your current location.</li>
    </ul>

  <h2>Usage</h2>
    <p>Run the script and leave it running in the background. You will receive email notifications if the ISS is overhead during the night.</p>

  <h2>License</h2>
    <p>This project is licensed under the <a href="LICENSE">MIT License</a>. See the LICENSE file for details.</p>

  <h2>Author</h2>
    <p>Created by [Your Name]. For inquiries and feedback, please contact [Your Email Address].</p>
</body>
</html>
