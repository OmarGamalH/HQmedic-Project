document.addEventListener("DOMContentLoaded" , function(){
    let errors = document.querySelectorAll(".error")
    let errors_length = errors.length
    errors_function(errors ,errors_length )
    document.querySelector("#patient_login_register_button").onclick = function(){
        show("patient_register")
    }
    document.querySelector("#patient_register_login_button").onclick = function(){
        show("patient")
    }
    document.querySelector("#doctor_login_register_button").onclick = function(){
        show("doctor_register")
    }
    document.querySelector("#doctor_register_login_button").onclick = function(){
        show("doctor")
    }
    document.querySelector("#register_select").onchange = function(){
    select("patient" , this)
    }
    document.querySelector("#doctor_register_select").onchange = function(){
        select("doctor" , this)
    }
    document.querySelector("#change_user").onclick = function(){
        window.location.href = '/login';
        show("categories")
        errors.forEach((element)=>{
            console.log(element)
            element.innerHTML = ""
        })
        
    }
    
    document.querySelectorAll(".category").forEach((element)=>{
        element.onclick = function(event){
            let parent = element.parentElement
            let category =  element.id
            console.log(category)
            element.style.backgroundColor = "lightgreen"
            element.style.color = "black"
            parent.querySelectorAll(".category").forEach(function(category){
                if (category != element){
                    category.style.backgroundColor = "lightred";
                    category.style.display = "none";
                }
            })
            setTimeout(()=>{
                element.style.display = "none"
                parent.style.display = "none"
            } , 500)
            show(category)
        }
    })
    document.querySelectorAll(".field").forEach((element) =>{
        let parent = element.parentElement
        parent.className = "field_div"
    })
    
})



function show(view){
    const navbar = document.querySelector("#navbar")
    const login_body = document.querySelector("#login_body")
    document.querySelectorAll("#login_body > div").forEach((element)=>{
        element.style.display = "none"
    })
    navbar.style.display = "flex"
    if (view == "categories"){
        let parent = document.querySelector("#categories")
        parent.style.display = "flex"
        parent.querySelectorAll("div").forEach((element)=>{
            element.style.display = "block"
            element.style.backgroundColor = "white"
            element.style.color = ""
        })
    }
    else if(view == "patient_register"){
        const  register_div = document.querySelector(`#${view}`)
        register_div.style.display = "block"
    }
    else if(view == "doctor_register"){
        const  register_div = document.querySelector(`#${view}`)
        register_div.style.display = "block"
    }
    else{
        const patient_div = document.querySelector(`#${view}_login`)
        patient_div.style.display = "block"
    }
}

function errors_function(errors , errors_length){
    const navbar = document.querySelector("#navbar")
    const login_body = document.querySelector("#login_body")
    document.querySelectorAll("#login_body > div").forEach((element)=>{
        element.style.display = "none"
    })
    navbar.style.display = "flex"
    for (let i = 0 ; i < errors_length ; i++){
    if(errors[i].innerHTML.length >= 1){
        errors[i].style.border = "1px lightgray solid"
        errors[i].parentElement.style.display = "block"
        document.querySelector("#categories").style.display = "none"
        break
    }else{
        if(i == errors_length - 1){
            show("categories")
        }
    }
}
}

function select(category , select_this){
    let value = select_this.value
        const form = document.querySelector(`#${category}_register_form`)
        let age_field = document.querySelector(`#${category}_register_age`)
        let username_field = document.querySelector(`#${category}_register_username`)
        let phonenumber = document.querySelector(`#${category}_register_phonenumber`)
        let fieldset = form.querySelector("fieldset")
        form.style.display = "block"
        console.log(form)
        console.log(age_field)
        console.log(username_field)
        console.log(fieldset)
        if (value == "Yes"){
            age_field.style.display = "none"
            username_field.style.display = "none"
            fieldset.style.display = "none"
            phonenumber.style.display = "none"
        }else{
            fieldset.style.display = "block"
            age_field.style.display = "block"
            username_field.style.display = "block"
            phonenumber.style.display = "block"

        }
}