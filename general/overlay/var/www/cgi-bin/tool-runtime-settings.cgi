#!/usr/bin/haserl
<%in p/common.cgi %>

<%
page_title="Camera runtime settings"

if [ "$REQUEST_METHOD" = "POST" ]; then
    case "$POST_action" in
        setfps)
            if echo "$POST_fps" | grep -qE '^[0-9]+$' && [ "$POST_fps" -ge 10 ] && [ "$POST_fps" -le 60 ]; then
                echo "setfps 0 $POST_fps" > /proc/mi_modules/mi_sensor/mi_sensor0
                echo "HTTP/1.1 200 OK"
                echo "Content-type: text/plain"
                echo ""
                echo "$POST_fps"
                exit
            fi
            ;;
        setbitrate)
            if echo "$POST_bitrate" | grep -qE '^[0-9]+$' && [ "$POST_bitrate" -ge 0 ] && [ "$POST_bitrate" -le 8192 ]; then
                curl -s "http://localhost/api/v1/set?video0.bitrate=$POST_bitrate" >/dev/null
                echo "HTTP/1.1 200 OK"
                echo "Content-type: text/plain"
                echo ""
                echo "$POST_bitrate"
                exit
            fi
            ;;
        setresolution)
            valid_resolutions="1920x1080 1280x720 854x480 1440x1080 960x720 640x480"
            if echo "$valid_resolutions" | grep -qw "$POST_resolution"; then
                yaml-cli -s .video0.size "$POST_resolution"
                echo "HTTP/1.1 200 OK"
                echo "Content-type: text/plain"
                echo ""
                echo "$POST_resolution"
                exit
            fi
            ;;
        restartmjpeg)
            if killall -1 majestic; then
                echo "HTTP/1.1 200 OK"
                echo "Content-type: text/plain"
                echo ""
                echo "Service restarted successfully"
                exit
            else
                echo "HTTP/1.1 500 Internal Server Error"
                echo "Content-type: text/plain"
                echo ""
                echo "Failed to restart service"
                exit
            fi
            ;;
    esac
    exit
fi
%>

<%in p/header.cgi %>

<style>
input[type="range"], select {
    outline: none;
    border: none;
    box-shadow: none;
    margin: 15px 0;
}
.control-group {
    margin-bottom: 25px;
}
.resolution-select {
    width: 100%;
    padding: 8px;
    border-radius: 4px;
    border: 1px solid #ddd;
}
.button_submit {
    margin-top: 20px;
    width: 100%;
    padding: 10px;
    background-color: #dc3545;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
.button_submit:hover {
    background-color: #c82333;
}
</style>

<script>
function updateControl(type, value) {
    fetch(window.location.href, {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: `action=set${type}&${type}=${value}`
    })
    .then(response => response.text())
    .then(newValue => {
        const element = document.getElementById(`${type}Value`);
        if (element) {
            element.textContent = `${newValue}${type === 'fps' ? ' FPS' : ' kbps'}`;
        }
    })
    .catch(error => console.error('Error:', error));
}

function setResolution(value) {
    fetch(window.location.href, {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: `action=setresolution&resolution=${value}`
    })
    .then(response => response.text())
    .then(res => {
        document.getElementById('currentResolution').textContent = res;
    })
    .catch(error => console.error('Error:', error));
}

function restartService() {
    fetch(window.location.href, {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: 'action=restartmjpeg'
    })
    .catch(error => console.error('Error:', error));
}
</script>

<div class="container mt-5">
    <div class="card border-0">
        <div class="card-body p-3">
            <!-- FPS Control -->
            <div class="control-group">
                <div class="d-flex align-items-center gap-3">
                    <input type="range" 
                           class="form-range" 
                           id="fpsSlider"
                           min="10" 
                           max="60" 
                           value="30"
                           oninput="updateControl('fps', this.value)">
                    <span class="badge bg-primary fs-5" id="fpsValue">30 FPS</span>
                </div>
            </div>

            <!-- Bitrate Control -->
            <div class="control-group">
                <div class="d-flex align-items-center gap-3">
                    <input type="range" 
                           class="form-range" 
                           id="bitrateSlider"
                           min="0" 
                           max="8192" 
                           step="256"
                           value="0"
                           oninput="updateControl('bitrate', this.value)">
                    <span class="badge bg-success fs-5" id="bitrateValue">0 kbps</span>
                </div>
            </div>

            <!-- Resolution Selector -->
            <div class="control-group">
                <label class="form-label">Video Resolution:</label>
                <select class="resolution-select" onchange="setResolution(this.value)">
                    <option value="1920x1080">1920x1080 16:9</option>
                    <option value="1280x720">1280x720 16:9</option>
                    <option value="854x480">854x480 16:9</option>
                    <option value="1440x1080">1440x1080 4:3</option>
                    <option value="960x720">960x720 4:3</option>
                    <option value="640x480">640x480 4:3</option>
                </select>
                <div class="mt-2">
                    Current: <span class="badge bg-info" id="currentResolution">-</span>
                </div>
            </div>

            <!-- Restart Service Button -->
            <div class="control-group">
                <button class="button_submit" onclick="restartService()">
                    Restart Majestic
                </button>
            </div>
        </div>
    </div>
</div>

<%in p/footer.cgi %>