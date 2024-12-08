var url = `http://${window.location.hostname}:${window.location.port}`
document.addEventListener("DOMContentLoaded" , function(){

    const add_advice_button = document.querySelector("#add_advice_button")
    if (add_advice_button){
        document.querySelector("#advices").style.display = "block";
        const add_advice_textarea = document.querySelector("#add_advice_textarea")
        add_advice_button.onclick = function(){
            let advice = add_advice_textarea.value
            let id = add_advice_textarea.dataset.id
            let error = document.querySelector(".error")
            add_advice_textarea.value = ""
            if (advice != "" && id){
                error.innerHTML = ""
            fetch(`${url}/add_advice` , {
                "method" : "POST",
                body : JSON.stringify({
                    "id" : id , 
                    "advice" : advice
                })          
            })}else{
                error.innerHTML = "Please Enter Advice"
            }
        }
    } 





    let menu = document.querySelector("#menu")
    let profile_image = document.querySelector("#profile_image")
    if (profile_image){
        profile_image.onerror = function(){
            profile_image.src = "/media/default.png"
        }
    }


    if (document.querySelector("#my_doctors")){
    document.querySelector("#my_doctors").addEventListener("click" , function(){
        if(document.querySelector("#simple_info")){
            let simple_info = document.querySelector("#simple_info")
            let general_info = document.querySelector("#general_info")
            let other_info = document.querySelector("#other_info")
            let body = document.querySelector("body")
            body.id = ""
            simple_info.style.display = "none"
            general_info.style.display = "none"
            other_info.style.display ="none"
            my_doctors("#my_doctors_profile")
        }else{
            let pending_doctors = document.querySelector("#pending_doctors")
            let all_advices = document.querySelector("#all_advices")
            if (pending_doctors){
                pending_doctors.style.display = "none"
            }
            if(all_advices){
                all_advices.style.display = "none"
            }
            my_doctors(".doctors")
        }

    })
    }
    
    



    
    menu.style.width = "0%"

    document.querySelector("#menu_button").onclick = function(){
        let doctors = document.querySelector("#doctors")
        if (menu.style.width == "0%"){
            menu.style.width = "30%"
            menu.style.display = "flex"
        }else{
            menu.style.width = "0%"
            menu.style.display = "none"
            }
    }

    show()
    add()
    like()
})


function render(status , doctors , specialist_info ){
    if (status == "patient"){
        
        // specialist div
        const specialist_div = document.createElement("div")
        const specialist = specialist_info["specialist"]
        const specialist_num = specialist_info["sum"]
        // h1 
        const h1 = document.createElement("h1")
        h1.innerHTML = specialist
        specialist_div.append(h1)
        // span
        const span = document.createElement("span")
        span.innerHTML = specialist_num
        span.className = "sum"
        h1.append(span)
        for ( let doctor of doctors){
            let doctor_specialist = doctor["fields"]["specialist"]
            let doctor_pk = doctor["pk"]
            let doctor_info = doctor["fields"]
            let user_info = doctor_info["user"][0]["fields"]
            if (doctor_specialist == specialist){
                // doctor div
                let doctor_div = document.createElement("div")
                doctor_div.className = "doctor_div"
                // first info div
                const first_doctor_info = document.createElement("div")
                first_doctor_info.className = "doctor"
                first_doctor_info.dataset.id = doctor_pk
                // info inside the first div
                const name = document.createElement("a")
                name.innerHTML = user_info["username"]
                name.href = `profile/doctor/${doctor_info["user"][0]["pk"]}`
                name.className = "name_h1"
                name.style.border = "none"
                const specialist_p = document.createElement("p")
                specialist_p.innerHTML = doctor_info["specialist"]
                const gender = document.createElement("p")
                gender.innerHTML = user_info["gender"]
                const likes = document.createElement("p")
                likes.innerHTML = doctor_info["likes"]
                likes.className = "likes"
                const buttons_div = document.createElement("div")
                const button_like = document.createElement("button")
                const button_add = document.createElement("button")
                const button_show = document.createElement("button")
               
                button_like.innerHTML = "like"
                button_add.innerHTML = "add"
                button_show.innerHTML = "show"
               
                button_like.className = "like button"
                button_add.className = "add button"
                button_show.className = "show button"
                
                button_like.dataset.id = doctor_pk
                button_add.dataset.id = doctor_pk
                buttons_div.append(button_like , button_add , button_show )
                first_doctor_info.append( name, specialist_p , gender , likes ,  buttons_div)
                // second doctor info
                const second_doctor_info = document.createElement("div")
                second_doctor_info.className = "doctor_info"
                const second_a = document.createElement("a")
                second_a.className = "name_h1"
                second_a.innerHTML = user_info["username"]
                second_a.href = `profile/doctor/${doctor_info["user"][0]["pk"]}`
                const first_h2 = document.createElement("h2")
                first_h2.style.marginLeft = "10px"
                first_h2.innerHTML = "Details: "
                // first detail div
                const first_detail_div = document.createElement("div")
                first_detail_div.className = "info"
                const first_image = document.createElement("img")
                first_image.src = "https://cdn-icons-png.flaticon.com/128/542/542689.png"
                first_image.className = "icon_info"
                let first_span = document.createElement("span")
                first_span.innerHTML = user_info["email"]
                first_detail_div.append(first_image , first_span)
                // second detail div
                const second_detail_div = document.createElement("div")
                second_detail_div.className = "info"
                const second_image = document.createElement("img")
                second_image.src = "https://cdn-icons-png.flaticon.com/128/15/15874.png"
                second_image.className = "icon_info"
                let second_span = document.createElement("span")
                second_span.innerHTML = user_info["phonenumber"]
                second_detail_div.append(second_image , second_span)
                // third detail div
                const third_detail_div = document.createElement("div")
                third_detail_div.className = "info"
                const third_image = document.createElement("img")
                third_image.src = "https://cdn-icons-png.flaticon.com/128/126/126473.png"
                third_image.className = "icon_info"
                let third_span = document.createElement("span")
                third_span.innerHTML = doctor_info["likes"]
                third_span.className = "likes"
                third_detail_div.append(third_image , third_span)
                




                second_doctor_info.append(second_a , first_h2 , first_detail_div , second_detail_div , third_detail_div)
                specialist_div.append(doctor_div)
                doctor_div.append(first_doctor_info , second_doctor_info)
            }
        }
    
        
        return specialist_div
    }   


}

function like(){
    document.querySelectorAll(".like").forEach((element)=>{
        let id = element.dataset.id
        fetch(`${url}/liked` , {
            method : "POST",
            body : JSON.stringify({
                "id" : id
            })
        }).then((response) => response.json()).then((data) =>{
            let liked = data["liked"]
            // liked is false (the doctor will be liked)
            if (liked == false){
                element.innerHTML = "like"
            }else{
                element.innerHTML = "Dislike"
            }
        })
        element.onclick = function(){
            fetch(`${url}/liked` , {
                method : "POST",
                body : JSON.stringify({
                    "id" : id
                })
            }).then((response) => response.json()).then((data) =>{
                let liked = data["liked"]
                // liked is false (the doctor will be liked)
                let parent = element.parentElement.parentElement.parentElement
                parent.querySelectorAll(".likes").forEach((ele)=>{
                    if (liked == false){
                        element.innerHTML = "Dislike"
                        ele.innerHTML = Number(ele.innerHTML) + 1
                        console.log(ele)
                    }else{
                        element.innerHTML = "like"
                        ele.innerHTML = Number(ele.innerHTML) - 1
                    }
                })
                
                fetch(`${url}/like` , {
                    method: "POST",
                    body : JSON.stringify({
                        "like" : !liked,
                        "id" : id  
                    })
                })
            })
        }
    })
}


function my_doctors(div){
    fetch(`${url}/my_doctors` , {
        method : "POST"
    }).then(request =>{return(request.json())}).then((data) => {
        let doctors = data["doctors"]
        let doctors_specialists = data["doctors_specialists"]
        const doctors_div = document.querySelector(div)
        doctors_div.innerHTML = ""
        if (doctors_specialists.length == 0){
            let h1 = document.createElement("h1")
            h1.className = "empty"
            h1.innerHTML = "No doctors were added yet"
            doctors_div.append(h1)
        }else{
            for (let specialist of doctors_specialists){
            doctors_div.append(render("patient" , doctors , specialist))
            }
            show()
            add()
            like()
        }
    })
}

function add(){
    document.querySelectorAll(".add").forEach((element) =>{
        let id = element.dataset.id
        fetch(`${url}/added` , {
            method : "POST",
            body : JSON.stringify({
                "id" : id
            })
        }).then(response => response.json()).then((data)=>{
            let added = data["added"]
                if (added == true){
                    element.innerHTML = "Remove"
                }else{
                    element.innerHTML = "Add"
                }
        })
        element.onclick = function(){
            fetch(`${url}/added` , {
                method : "POST",
                body : JSON.stringify({
                    "id" : id
                })
            }).then((response) => response.json()).then((data)=>{
                let added = data["added"]
                if (added == true){
                    element.innerHTML = "Add"
                }else{
                    element.innerHTML = "Remove"
                }
                fetch(`${url}/add` , {
                    method : "POST",
                    body : JSON.stringify({
                        "add" : !added,
                        "id" : id
                    })
                }).then(response =>response.json()).then((data)=>{
                })
            })
        }
    })

}

function show(){
    document.querySelectorAll(".show").forEach((element) =>{
        let parent = element.parentElement.parentElement.parentElement
        let info = parent.querySelector(".doctor_info")
        element.onclick = function(){
            if (info.style.display == "" || info.style.display == "none"){
                info.style.display = "block"
            }else{
                info.style.display = "none"
            }
        }
    })
}

function liked(id){
    fetch(`${url}/liked` , {
        method : "POST",
        body : JSON.stringify({
            "id" : id
        })
    }).then((response) => response.json()).then((data) =>{
        let liked = data["liked"]
        // liked is false (the doctor will be liked)
        if (liked == false){
            return "like"
        }else{
            return "Dislike"
        }
    })

}
function massage(){
    let buttons = document.querySelectorAll(".massage")
    buttons.forEach((element) =>{
        element.onclick = function(){

        }
    })
}