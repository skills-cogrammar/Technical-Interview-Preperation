export function getPageHeading(){    
    const pageHeadingContainer = document.createElement("section");
    pageHeadingContainer.className = "page-heading";

    const header = document.createElement("h1");    
    header.innerText = "Live Events";

    pageHeadingContainer.appendChild(header)
    return pageHeadingContainer;
}

export function getEventsContainer(events){
    const eventsContainer = document.createElement("section");
    eventsContainer.className = "event-list-container";
    
    const eventsList = document.createElement("ul");    
    
    for (let event of events){
        const eventCard = createEventCard(event);
        eventsList.appendChild(eventCard);
    }

    eventsContainer.appendChild(eventsList);

    return eventsContainer;
}

function createEventCard(event){
    const eventCard = document.createElement("li");
    eventCard.className = "event-card";

    const eventTitle = document.createElement("h2");
    eventTitle.className = "event-title"
    eventTitle.innerText = event.title;

    const eventDescription = document.createElement("p");
    eventDescription.className = "event-description"
    eventDescription.innerText = event.description;

    const eventDate = document.createElement("p");
    eventDate.className = "event-date"
    eventDate.innerText = event.date;

    eventCard.appendChild(eventTitle);
    eventCard.appendChild(eventDate);
    eventCard.appendChild(eventDescription);    

    return eventCard;
}
