const API_KEY = '&apikey=e73fc890'

$(document).ready(() => {
    $('#searchForm').on('submit', (e) => {
        let searchText = $('#searchText').val();
        console.log(searchText);
        getMovie(searchText);
        return false;
        
    });
});

async function getMovie(text) {
    const response = await fetch('http://www.omdbapi.com/?s=' + text + API_KEY);
    const movies = await response.json(); //extract JSON from the http response
    let output = '';
    console.log(movies);
    movies.Search.forEach(movie => {
        output += `
        <div class="col-md-3 col-sm-4">
        <div class="well text-center">
          <img src="${movie.Poster}">
          <h5>${movie.Title}</h5>
          <a onclick="movieSelected('${movie.imdbID}')" class="btn btn-primary" href="#">Movie Details</a>
        </div>
        </div>
        `;
    });

    $('#movies').html(output);
}