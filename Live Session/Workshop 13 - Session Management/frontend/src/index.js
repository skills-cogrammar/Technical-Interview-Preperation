import { getEventsContainer, getPageHeading } from "./views/events.view.js"
import {  getAuthenticatedNavbar} from "./views/navbar.view.js"


const root = document.getElementById("root");
const userAuth = {
    isAuthenticated: false,
    role: null
}

render()

function render(){
    generalUserContent();    
    generateNavBar();
}

function generateNavBar(){
    const routes = document.getElementById("routes")
    routes.appendChild(getAuthenticatedNavbar())
}

async function generalUserContent(){
    const events = await getEvents();

    root.appendChild(getPageHeading());
    root.appendChild(getEventsContainer(events));
}

async function getEvents(){
    const response = await fetch("http://localhost:8000/events")
    const events = await response.json();
    return events
}