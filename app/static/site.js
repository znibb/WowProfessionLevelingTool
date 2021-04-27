$( document ).ready(function() {
    displaySchoolOptions()

    var $range = $(".js-range-slider"),
        $inputFrom = $(".js-input-from"),
        $inputTo = $(".js-input-to"),
        instance,
        min = 1,
        max = 300,
        from = $inputFrom.prop("value"),
        to = $inputTo.prop("value");

    $range.ionRangeSlider({
        skin: "round",
        type: "double",
        min: min,
        max: max,
        from: from,
        to: to,
        hide_from_to: true,
        hide_min_max: true,
        onStart: updateInputs,
        onChange: updateInputs
    });
    instance = $range.data("ionRangeSlider");

    function updateInputs(data) {
        console.log(data)
        from = data.from;
        to = data.to;

        if (from === to)
        {
            from = to - 1;
            instance.update({
                to: to,
                from: from
            });
        }

        $inputFrom.prop("value", from);
        $inputTo.prop("value", to);
    }

    $inputFrom.on("input", function () {
        var val = $(this).prop("value");

        // validate
        if (val < min) {
            val = min;
        } else if (val >= to) {
            val = to - 1;
        }

        instance.update({
            from: val
        });
    });

    $inputTo.on("input", function () {
        var val = $(this).prop("value");

        // validate
        if (val <= from) {
            val = from + 1;
        } else if (val > max) {
            val = max;
        }

        instance.update({
            to: val
        });
    });
});

$(document).on('change', '#profession', function() {
    displaySchoolOptions();
})

function displaySchoolOptions() {    
    $(".schoolOptions").hide();
    var selectedProfession = $('#profession').prop("value");
    $("." + selectedProfession + "School").show();
}