x = 0;

function usersinfo(){
   
    if(x==0){
        document.getElementById("userbtns").style.display = "block"
        return x=1;
    }
    else if(x==1){
        document.getElementById("userbtns").style.display = "none"
        return x=0;
    }
}

function addclass(){

    document.getElementById("createclasses").style.display = "block"

}

function closeclass(){

    document.getElementById("createclasses").style.display = "none"

}

function addsemester(){

    document.getElementById("createsemester").style.display = "block"

}

function closesemester(){

    document.getElementById("createsemester").style.display = "none"

}


