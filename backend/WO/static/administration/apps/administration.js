var dataTableElement = function(idElement,urlService){
    $('#'+idElement).DataTable({
                responsive: true,
                sPaginationType: "full_numbers", //type of pagination
                bfilter: true,
                bPaginate: true, //pagination
                bSort: true,
                bProcessing:true,//Text processing when child records a lot
                bInfo: true,//Show results information
                "iDisplayLength": 10, //Pagination
                "lengthMenu": [[10, 25, 50,100, -1], [10, 25, 50,100, "Todos"]], //selector de mostrar registros/
                bServerSide: true,
                sAjaxSource: urlService,
                columnDefs: [
                    {targets: [0], visible: false},
                    {
                        targets: 13,
                        render: function (data, type, full, meta) {
                            //console.log("algo", full[0]);
                            console.log('sss')
                            var opciones = $('<span>')
                            var edit = null;
                            var detail = null;
                            edit = $('<a href="/administration/edit/order/' + full[0] + '/" class="btn" title="Edit"> <button class="btn btn-warning btn-sm"> <i class="fa fa-pencil-square-o fa-lg" aria-hidden="true"></i></button></a>')
                            detail = $('<a href="/administration/detail/order/' + full[0] + '/" class="btn" title="Detail"><button class="btn btn-danger btn-sm"><i class="fa fa-eye fa-lg" aria-hidden="true"></i></button></a>');
                            opciones.append(edit, detail);
                            return opciones.html();
                        }
                    }
                ],

            });
    };
