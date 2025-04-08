async function load_header() {
    let header = await eel.load_component()() //'/src/components/header.html'
    return header
}

async function base_header(props) {
    return await load_header() //.replaceAll('<children/>', props?.children)
}