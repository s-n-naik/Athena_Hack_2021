function show_results(){
    let results = document.querySelector("#upload")

    if (isset($_POST["button"])){
        $("#results").show()
    }else{
        $("#results").hide()
        $("#results").val("")
    }
}
