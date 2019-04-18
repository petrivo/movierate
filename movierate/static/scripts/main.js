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
          <a onclick="movieSelected(this,'${movie.imdbID}')" class="btn btn-primary mbtn">Movie Details</a>
        </div>
        </div>
        `;
    });

    $('#movies').html(output);
}

async function renderMovie(id) {
    console.log('rendering');
    const response = await fetch('http://www.omdbapi.com/?i=' + id + API_KEY);
    const movie = await response.json(); //extract JSON from the http response
    let output = `
        <div class="col-md-3 col-sm-4">
        <div class="well text-center">
          <img src="${movie.Poster}">
          <h5>${movie.Title}</h5>
          <a onclick="likeThisMore(this,'${movie.imdbID}')" class="btn btn-primary mbtn">Prefer</a>
        </div>
        </div>
        `;
    $('#movies').append(output);
}

// $(document.body).on("click",".mbtn", function () {
//     var addressValue = $(this).attr("href");
//     console.log(addressValue );
//     $(this).attr('class', 'btn btn-outline-success my-2 my-sm-0');
// });

function movieSelected(obj,movieSelected){
    console.log(obj);
    console.log(movieSelected);
    $.ajax({
        type: "POST",
        url: '/add_movie',
        data: JSON.stringify({'movie_id': movieSelected}),
        // dataType: 'json', //commented out to have success running
        contentType: 'application/json',
        success: () => {
            console.log('success');
            $(obj).attr('class', 'btn btn-outline-success my-2 my-sm-0');
            $(obj).text('Selected')

        },
        error: () => {
            $(obj).attr('class', 'btn btn-danger my-2 my-sm-0');
        }
    });
}