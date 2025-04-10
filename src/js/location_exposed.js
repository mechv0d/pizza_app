eel.expose(go_to);
eel.expose(reload);

function go_to(url) {
    location.href = url;
    console.log(url)
}

function reload() {
    location.reload();
}