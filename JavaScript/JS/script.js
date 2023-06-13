
var page = document.getElementById("mainContent")

function changePage(v){
    if (v == 1){
        page.innerHTML = "HomePage";
    } else if(v == 2) {
        page.innerHTML = "Seccond page";
    }

}