$(document).ready(function () {
    var form = $('#form__order');
    form.on('submit', function (e) {
        id = '_' + Math.random().toString(36).substr(2, 9);
        e.preventDefault();

        var radios = $('input[type="radio"][name="dough"]');
        var temp = radios.filter(":checked");
        arr = getArr(id, temp);
        if(arr[1] === undefined || arr[2] === undefined){
            alert("Choose a dough!")
        }
        else {
            $.ajax({
                url: 'order_create/',
                data: {'data': arr},
                type: "POST",
                success: function (data) {

                }
            });


            $('.get__number').each(function () {

                var v = $(this).val();
                var n = $(this).data("ingredient_name");
                var arr = [id, n, v];

                $.ajax({
                    url: 'order_create/',
                    data: {'data': arr},
                    type: "POST",
                    success: function (data) {

                    }
                });
            });
        }
        return false;
    });
});

function getArr(id, thisParameter) {
    var v = thisParameter.val();
    var n = thisParameter.data("ingredient_name");
    return [id, n, v];
}
