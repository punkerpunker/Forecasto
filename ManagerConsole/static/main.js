const user_input = $("#user-input")
const search_icon = $('#search-icon')
const players_div = $('#replaceable-content')
const player_picker = '.btn-secondary'
const player_card_div = $('#player-card')
const endpoint = '/'
const delay_by_in_ms = 300
let scheduled_function = false


let ajax_call = function (endpoint, div, request_parameters, callback) {
    $.getJSON(endpoint, request_parameters)
        .done(response => {
            // fade out the artists_div, then:
            div.fadeTo('fast', 0).promise().then(() => {
                // replace the HTML contents
                div.html(response['html_from_view'])
                // fade-in the div with new contents
                div.fadeTo('fast', 1)
                callback();
                // stop animating search icon
                search_icon.removeClass('blink')
            })
        })
}

let change_playoff_switcher = function (value) {
    $("input[type=\'radio\']", '#playoff-switcher').val([value], '#playoff-switcher')
}

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

        $('button').removeClass('active');
        button.addClass('active');
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




