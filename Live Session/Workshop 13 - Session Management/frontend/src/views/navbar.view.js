export function getAuthenticatedNavbar(){
    const routesList = document.createElement("li");
    routesList.classList.add("nav-item");
    
    while (routesList.firstChild) {
        routesList.removeChild(routesList.firstChild);
    }
    
    const userAuth = localStorage.getItem("authenticated");
    console.log(userAuth)

    if (!userAuth){
        routesList.appendChild(getLoginLink())
    }        
    else {
        routesList.appendChild(getCreateEvent());
        routesList.appendChild(getLogoutLink());
    }

    return routesList;    
}

function getLoginLink(){
    const loginLink = document.createElement("a");
    loginLink.classList.add("nav-link");    
    loginLink.textContent = "Login";

    loginLink.addEventListener('click', () => {
        const username = prompt("Email");
        const password = prompt("Password");

        fetch("http://localhost:8000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: username,
                password: password
            })
        }).then((response) => {
            if (response.ok){
                return response.json();
            }
            else {
                throw new Error("Login failed");
            }
        }).then((data) => {
            localStorage.setItem("sessionToken", data.token);
            localStorage.setItem("authenticated", true);
            window.location.reload();
        }).catch((err) => alert("something went wrong"));
    });
    

    return loginLink;
}

function getLogoutLink(){
    const logoutLink = document.createElement("a");
    logoutLink.classList.add("nav-link");    
    logoutLink.textContent = "Logout";

    logoutLink.addEventListener("click", () => {
        localStorage.removeItem("authenticated")
        localStorage.removeItem("sessionToken");

        window.location.reload();
    })

    
    
    return logoutLink;
}

function getCreateEvent(){
    const manageAccountLink = document.createElement("a");
    manageAccountLink.classList.add("nav-link");
    manageAccountLink.textContent = "Create Event";

    manageAccountLink.addEventListener('click', () => {
        const title = prompt("Title");
        const description = prompt("Description");
        const date = prompt("Date");

        fetch("http://localhost:8000/events", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${localStorage.getItem("sessionToken")}`
            },
            body: JSON.stringify({
                title: title,
                description: description,
                date: date
            })
        }).then((response) => {
            if (response.ok){
                return response.json();
            }
            else {
                throw new Error("Event creation failed");
            }
        }).then((data) => {
            alert("Event created successfully");
        }).catch((err) => alert("something went wrong"));
    });

    return manageAccountLink;
}