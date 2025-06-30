
document.addEventListener('DOMContentLoaded', () => {
  const isIndex = document.body.classList.contains('home-page');
  const alllands = document.body.classList.contains('AllLands');

  //the if statment on the index(home) page.html
  if (isIndex) {
    const container = document.querySelector('.lands-container');
    const searchInput = document.getElementById('search-location');
    const searchIcon = document.getElementById('search-Icon');
    const noResult = document.querySelector('.No-result')
    //store all lands for filtering later
    let allLands = [];
    // fetch and display lands 
    fetch('/api/lands')
    .then(res => res.json())
    .then(lands => {
      allLands = lands;
      console.log(allLands);
      
      displayLands(lands.slice(0, 20));
    });

    //function to display land cards
    function displayLands (landsToDisplay) {
      // clear current list/lands
      if (landsToDisplay.length === 0) {
        noResult.style.display = 'block';
        return;
      }else{
        noResult.style.display = 'none';
    
      container.innerHTML = ''; 
      landsToDisplay.forEach(land => {
        container.innerHTML += `<a href="/land/${land.id}"><div class="land-card"> 
                                <h3>${land.description}</h3>
                                <img src="${land.mainImage}" alt="${land.title}">
                                <h4>Titre: ${land.title}</h4>
                                <p>Emplacement: ${land.location}</p>
                                <p>Prix: ${land.price}</p>
                                <p>Status: ${land.status}</p>
                                <a href="/land/${land.id}">Voir plus</a>
                                </div></a> `;   
                                
      });
    }
    
    }

    //Search By Location In the Home Code
    searchIcon.addEventListener('click', () => {
      performSearch();
    });
    searchInput.addEventListener('keydown', (event) =>{
      if (event.key === 'Enter') {
        performSearch();
      }
    });

    function performSearch() {
      const searchTerm = searchInput.value.trim().toLowerCase();
      const Filterlands = allLands.filter(land => 
        land.location?.toLowerCase().includes(searchTerm)
      );
      displayLands(Filterlands)
    }
    
  }

  if (alllands) {
    const container = document.querySelector('.all-Lands');
    const searchInput = document.getElementById('search-location');
    const searchIcon = document.getElementById('search-Icon');
    const noResult = document.querySelector('.No-result');
    let allLands = [];
  fetch('/api/lands')
  .then(jalloh => jalloh.json())
  .then(Barrie => {
    allLands = Barrie;
    displayLands(allLands);

  });

  // console.log(displayLands)
    function displayLands(landsToDisplay) {
      if (landsToDisplay.length === 0) {
        noResult.style.display = 'block';
        return;
      }else{
        noResult.style.display = 'none';
      
      container.innerHTML = '';
      landsToDisplay.forEach(land =>{ 
        container.innerHTML += `<a href="/land/${land.id}"> <section class="Lands-card"> 
          <h3>${land.description}</h3>
         <img src="${land.mainImage}" alt="${land.title}">
        <h2> Title: ${land.title}</h2> 
        <h2> Status: ${land.status}</h2> 
        <p> <strong> Emplacement: </strong>${land.location} </p> 
        <p> <strong> Prix: </strong>${land.price} </p> 
        <a href="/land/${land.id}" class="view-more-btn">Voir plus</a> </section> </a>`;
        
      });
    }
  }
    // Code To Search for a country by Location in the all Lands Page
searchIcon.addEventListener('click', () =>  {
    searchKey()
  });
     searchInput.addEventListener('keydown', (event) =>{
      if (event.key === 'Enter') {
        searchKey();
      }
     });

     function searchKey() {
      const searchTerm = searchInput.value.trim().toLowerCase();
      const Filterlands = allLands.filter(land => 
        land.location?.toLowerCase().includes(searchTerm)
      );
      displayLands(Filterlands);
     }
  };

})


function initMap() {
  const mapDiv = document.getElementById("map");
  const lat = parseFloat(mapDiv.getAttribute("data-lat"));
  const lng = parseFloat(mapDiv.getAttribute("data-lng"));

  if (!isNaN(lat) && !isNaN(lng)) {
    const location = { lat: lat, lng: lng };
    const map = new google.maps.Map(mapDiv, {
      zoom: 15,
      center: location,
    });
    new google.maps.Marker({ position: location, map: map });
  } else {
    console.error("Invalid coordinates:", lat, lng);
  }
}

let navbtn = document.getElementById('Menue-links')
function MenueFunction() {
  navbtn.classList.toggle('Show-Menue')
}