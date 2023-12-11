

var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('update', function(data) {
    updateCurlCount(data.rep_count);
});

function updateCurlCount(repCount) {
    var curlCountElement = document.getElementById('curl_count');
    curlCountElement.innerText = 'Number of Curls Tracked: ' + repCount;
}

document.addEventListener('keydown', function (event) {
    if (event.key === 'q' || event.key === 'Q') {
        // Stop the tracking by setting the source to an empty string
        document.getElementById('video_feed').src = '';
        window.location.href = "/";
    }
});

document.addEventListener('DOMContentLoaded', function () {
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('update', function (data) {
        // Update the content of the paragraph with the new remaining curls value
        document.getElementById('remaining_curls').innerText = 'Remaining Curls: ' + data.remaining_curls;
    });
});
