async function load_component(path) {
    let component = await eel.load_component(path)()
    component.then(res => {
        return res
    })
}

async function base_header(swaps, children) {
    let header_promise = load_component('src/components/header.html')
    header_promise.then(h => {

        let header = h.replaceAll("<children/>", children ?? '')
        var my_script = document.querySelector('#header');
        console.log(my_script)
        var elm = document.createElement('header');
        elm.innerHTML = header;
        my_script.parentNode.insertBefore(elm, my_script.nextSibling);
    })
}