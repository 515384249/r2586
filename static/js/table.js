$(function () {
    let $table = $('#ArbetTable');
    let $button = $('#mybtn_add');
    let $getTableData = $('#mybtn_save');
    let $detbnt = $('#mybtn_delete');

    $button.click(function () {
        $table.bootstrapTable('insertRow', {
            index: 0,
            row: {}
        });
    });

    $table.bootstrapTable({
        clickEdit: true,
        showToggle: true,
        pagination: false,       //显示分页条
        showColumns: true,
        showPaginationSwitch: false,     //显示切换分页按钮
        showRefresh: true,      //显示刷新按钮
        clickToSelect: true,  //点击row选中radio或CheckBox
        // columns: [{
        //     checkbox: true
        // },
        //     {
        //         field: 'id',
        //         title: 'Item ID'
        //     },
        //     {
        //         field: 'name',
        //         title: 'Item Name'
        //     },
        //     {
        //         field: 'price',
        //         title: 'Item Price'
        //     },],
        /**
         * @param {点击列的 field 名称} field
         * @param {点击列的 value 值} value
         * @param {点击列的整行数据} row
         * @param {td 元素} $element
         */



        onClickCell: function (field, value, row, $element) {
            console.log(row)
             console.log($element.checkbox)
            if ($element == true) {
                    alert("we get subbox")
            }
            $element.attr('contenteditable', true);
            $element.blur(function () {
                let index = $element.parent().data('index');
                let tdValue = $element.html();
                console.log(tdValue)
                saveData(index, field, tdValue);
            })
        }
    });

    // $getTableData.click(function () {
    //     alert(JSON.stringify($table.bootstrapTable('getSelections')));
    //     var myarray = new Array();
    //     myarray = JSON.stringify($table.bootstrapTable('getSelections'))
    //
    //
    //
    //
    // });



//保存
$(document).ready(function () {
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            function csrfSafeMethod(method) {
                // these HTTP methods do not require CSRF protection
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }

            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                var csrftoken = getCookie('csrftoken');
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    $getTableData.click(function () {


        var myarray = new Array();
        myarray = JSON.stringify($table.bootstrapTable('getSelections'));
        alert(myarray)
        // var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
        $.ajax({

            type: "POST",
            data: {

                "type": "save",
                "data": myarray,
            },
            url: '/kjfs_edit/', //后台处理函数的url 这里用的是static url 需要与urls.py中的name一致
            cache: false,

            dataType: "html",
            success: function (result) {
                alert("tiaozhuan");
                window.location.reload()
            },
            error: function () {
                alert("false");
            }
        });
        return false;
    });


});

//s刪除
    $(document).ready(function () {
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            function csrfSafeMethod(method) {
                // these HTTP methods do not require CSRF protection
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }

            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                var csrftoken = getCookie('csrftoken');
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    $detbnt.click(function () {


        var myarray = new Array();
        myarray = JSON.stringify($table.bootstrapTable('getSelections'));
        alert(myarray)
        // var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
        $.ajax({

            type: "POST",
            data: {

                "type": "del",
                "data": myarray,
            },
            url: '/kjfs_edit/', //后台处理函数的url 这里用的是static url 需要与urls.py中的name一致
            cache: false,

            dataType: "html",
            success: function (result) {
                alert("tiaozhuan");
                window.location.reload()
            },
            error: function () {
                alert("false");
            }
        });
        return false;
    });


});






    function saveData(index, field, value) {
        $table.bootstrapTable('updateCell', {
            index: index,       //行索引
            field: field,       //列名
            value: value        //cell值
        })
        console.log(index, field, value)
    }

});
// ---------------------
// 作者：帝尊菜鸟
// 来源：CSDN
// 原文：https://blog.csdn.net/dizuncainiao/article/details/81742971
// 版权声明：本文为博主原创文章，转载请附上博文链接！

function SaveImport() {

            var list = [];//构造集合对象
            var rows = $import.bootstrapTable('getSelections');
            for (var i = 0; i < rows.length; i++) {
                list.push({
                    'Name': rows[i].Name, 'Mobile': rows[i].Mobile, 'Email': rows[i].Email, 'Homepage': rows[i].Homepage,
                    'Hobby': rows[i].Hobby, 'Gender': rows[i].Gender, 'Age': rows[i].Age, 'BirthDate': rows[i].BirthDate,
                    'Height': rows[i].Height, 'Note': rows[i].Note
                });
            }

            if (list.length == 0) {
                showToast("请选择一条记录", "warning");
                return;
            }

            var postData = { 'list': list };//可以增加其他参数，如{ 'list': list, 'Rucanghao': $("#Rucanghao").val() };
            postData = JSON.stringify(postData);

            $.ajax({
                url: '/TestUser/SaveExcelData',
                type: 'post',
                dataType: 'json',
                contentType: 'application/json;charset=utf-8',
                traditional: true,
                success: function (data) {
                    if (data.Success) {
                        //保存成功  1.关闭弹出层，2.清空记录显示 3.刷新主列表
                        showToast("保存成功");

                        $("#import").modal("hide");
                        $(bodyTag).html("");
                        Refresh();
                    }
                    else {
                        showToast("保存失败:" + data.ErrorMessage, "error");
                    }
                },
                data: postData
            });
        }