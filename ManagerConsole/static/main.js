const user_input = $("#user-input")
const search_icon = $('#search-icon')
const players_div = $('#replaceable-content')
const player_picker = '.btn-secondary'
const player_card_div = $('#player-card')
const endpoint = '/'
const delay_by_in_ms = 300
let scheduled_function = false

let ajax_call = function (endpoint, div, request_parameters, callback = NaN) {
    $.getJSON(endpoint, request_parameters)
        .done(response => {
            div.fadeTo(200, 0).promise().then(() => {
                div.html(response['html_from_view'])
                if (typeof callback === "function") {
                    callback();
                }
                div.fadeTo(200, 1);
                search_icon.removeClass('blink');
            })
        })
}

let change_playoff_switcher = function (value) {
    $("input[type=\'radio\']", '#playoff-switcher').val([value], '#playoff-switcher')
}

$(document).on('click', '.custom-control-input', function () {
    let playoff_switcher_value = $('input[type=\'radio\']:checked', '#playoff-switcher').val() || 'regular';
    let player_id = $(".selection_button_active").attr('id')
    let div = $('#graph')

    const request_parameters = {
        player_id: player_id, // value of user_input: the HTML element with ID user-input
        div: div.attr('id'),
        playoff_switcher: playoff_switcher_value,
    }
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }
    ajax_call(endpoint, div, request_parameters, function() {
        change_playoff_switcher(playoff_switcher_value)});
})

$(document).on('click', '#predict-button', function () {
    let playoff_switcher_value = $('input[type=\'radio\']:checked', '#playoff-switcher').val() || 'regular';
    let player_id = $(".selection_button_active").attr('id')
    let div = $('#graph')
    let games = $("#num-games-field").val()

    const request_parameters = {
        player_id: player_id, // value of user_input: the HTML element with ID user-input
        div: div.attr('id'),
        playoff_switcher: playoff_switcher_value,
        predict: true,
        games: games,
    }
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }
    ajax_call(endpoint, div, request_parameters, function() {
        change_playoff_switcher(playoff_switcher_value)});
})

user_input.keyup(function () {
    const request_parameters = {
        player_name: $(this).val(), // value of user_input: the HTML element with ID user-input
        div: 'user-input'
    }
    // start animating the search icon with the CSS class
    search_icon.addClass('blink')

    // if scheduled_function is NOT false, cancel the execution of the function
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }

    // setTimeout returns the ID of the function to be executed
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, players_div, request_parameters)
})

$(document).ready(function() {
    $(document).on('click', player_picker, function () {
        let button = $('#' + this.id);
        let playoff_switcher_value = $('input[type=\'radio\']:checked', '#playoff-switcher').val() || 'regular';

        $('button').removeClass('selection_button_active');
        button.addClass('selection_button_active');
        const request_parameters = {
            player_id: this.id, // value of user_input: the HTML element with ID user-input
            div: 'player-pick',
            playoff_switcher: playoff_switcher_value,
        }
        // start animating the search icon with the CSS class
        search_icon.addClass('blink')
         // if scheduled_function is NOT false, cancel the execution of the function
        if (scheduled_function) {
            clearTimeout(scheduled_function)
        }

        // setTimeout returns the ID of the function to be executed
        ajax_call(endpoint, player_card_div, request_parameters, function() {
            change_playoff_switcher(playoff_switcher_value)});
    })
})

$(document).ready(function() {
    $(document).on('input', '#num-games-slider', function() {
        let num_games_field = $("#num-games-field");
        num_games_field.val(this.value)
    })
})

$(document).ready(function() {
    $(document).on('keyup', '#num-games-field', function() {
        let num_games_slider = $("#num-games-slider");
        num_games_slider.val(this.value)
    })
})

$(document).ready(function() {
    $(document).on('keyup', '#num-games-field', function() {
        let num_games_field = $("#num-games-field");
        let max = parseInt(num_games_field.attr('max'));

        if (parseInt(this.value) > max) {
            num_games_field.val(max)
        }
    })
})
