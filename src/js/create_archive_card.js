async function create_archive_card(fName, fNumb, fClient, fWeight, fCal, fPrice, fTips, fIngredients, fTakeTime, fTaker, fReadyState, fReadyTime, fArchiveTime) {
    let card = await eel.create_archive_card(fName, fNumb, fClient, fWeight, fCal, fPrice, fTips, fIngredients, fTakeTime, fTaker, fReadyState, fReadyTime, fArchiveTime)()
    return card
}

async function load_archive_cards(){
    return await eel.load_archive_cards()()
}

async function load_food_cards(){
    return await eel.load_food_cards()()
}