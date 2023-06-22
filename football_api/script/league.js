setTimeout(() => {
    const teams = document.getElementsByClassName("wg_nowrap")
    console.log(teams)
    for(let team of teams){
        team.addEventListener("click",function(){
            window.location.href = "/team.html"
        })
    }
}, 5000);

