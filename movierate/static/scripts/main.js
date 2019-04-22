const API_KEY = '&apikey=e73fc890';

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

async function renderMovie(database_id, movie_id, preferred) {
    console.log('rendering');
    const response = await fetch('http://www.omdbapi.com/?i=' + movie_id + API_KEY);
    const movie = await response.json(); //extract JSON from the http response
    let output = `
        <div class="col-md-3 col-sm-4">
        <div class="well text-center">
          <img src="${movie.Poster}">
          <h5>${movie.Title}</h5>
            <a onclick="moviePreferred(this, '${database_id}', '${preferred}')" class="btn btn-primary mbtn">Prefer</a>
          
        </div>
        </div>
        `;
    $('#movies').append(output);
}

function moviePreferred(obj, database_id, preferred){
    console.log(database_id);
    $.ajax({
        type: "POST",
        url: '/preferred_movie',
        data: JSON.stringify({'database_id': database_id, 'preferred': preferred}),
        // dataType: 'json', //commented out to have success running
        contentType: 'application/json',
        success: () => {
            console.log('success');
            $(obj).attr('class', 'btn btn-outline-success my-2 my-sm-0');
            $(obj).text('Selected')
            location.reload()
        },
        error: () => {
            $(obj).attr('class', 'btn btn-danger my-2 my-sm-0');
        }
    });
}

async function getById(e){
    const response = await fetch('http://www.omdbapi.com/?i=' + e + API_KEY);
    const movie = await response.json(); //extract JSON from the http response
    return movie.Title;
}

async function renderPreferenceList(data){
    console.log(data);
    let output = '';
    data.forEach( e =>{
        output =`<li id='${e}' class="list-group-item"></li>`;
        $('#movies_inorder').append(output);
    });
    data.forEach(async e =>{
        $(`#${e}`).text(await getById(e));
    });
}

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