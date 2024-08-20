import time
from phew import server, connect_to_wifi
from private import *
import random
import b64 as base64


def generateTimeStamp():
    now = time.localtime()
    print(now)
    stamp = f"{now[0]}-{now[1]}-{now[2]} {now[3]}.{now[4]}-{now[5]}"
    return stamp

connect_to_wifi(WIFI_SSID, WIFI_PASSWORD)

@server.route("/random", methods=["GET"])
def random_number(request):
    min = int(request.query.get("min", 0))
    max = int(request.query.get("max", 100))
    return str(random.randint(min, max))

@server.route("/form", methods=["GET"])
def form(request):
    return '''
        <script>
            function getBase64(file, dest) {
                var reader = new FileReader();
                reader.readAsDataURL(file);
                reader.onload = function () {
                    console.log(reader.result);
                    document.querySelector(dest).value = reader.result
                };
                reader.onerror = function (error) {
                    console.log('Error: ', error);
                };
            }
        </script>
        <form enctype="multipart/form-data" action="/upload" method="POST" accept-charset="utf-8" onsubmit="event.preventDefault(); document.querySelector('#uplf').remove(); this.submit(); ">
            <input name="uploadedfile" type="file" id="uplf" onchange="getBase64(this.files[0], '#b64f')" /><br />
            <input name="base64file" type="hidden" id="b64f" /><br />
            <input type="submit" value="Upload File" />
        </form>
        '''

@server.route("/upload", methods=["POST"])
def post(request):
    #print(request.form)
    #print(str(type(request.form)) + str(request.form))
    fn = f'/sd/{generateTimeStamp()}.bin'
    b64 = request.form['base64file']
    
    header, data_part = b64.split(',', 1)
    if 'base64' in header:
        data = base64.b64decode(data_part)
    else:
        data = data_part.encode('utf-8')

    with open(fn, 'wb') as f:
        f.write(data)

    return f'<h1>Uploaded to {fn}.</h1>'

@server.catchall()
def catchall(request):
    return "Not found", 404


SERVER = server