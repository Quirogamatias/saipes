function listadoPorcentaje(){
    $.ajax({
        url: "/institucion/listar_porcentajes/",
        type: "get",
        dataType: "json",
        success: function(response){
            if($.fn.DataTable.isDataTable('#tabla_porcentajes')){
                $('#tabla_porcentajes').DataTable().destroy();
            }
            $('#tabla_porcentajes tbody').html("");
            for(let i = 0;i < response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + (i+1) + '</td>';
                if (response[i]["fields"]['id_materia'] == ''){
                    fila += '<td> Desconocido </td>';
                } else {
                    fila += '<td>' + response[i]["fields"]['id_materia'] + '</td>';       
                }
                if (response[i]["fields"]['id_alumno'] == ''){
                    fila += '<td> Desconocido </td>';
                } else {
                    fila += '<td>' + response[i]["fields"]['id_alumno'] + '</td>';       
                }
                fila += '<td>' + response[i]["fields"]['promedio'] + '</td>';
                fila += '</tr>';
                $('#tabla_porcentajes tbody').append(fila);
            }             
            $('#tabla_porcentajes').DataTable({
                language: {
                    "decimal": "",
                    "emptyTable": "No hay información",
                    "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                    "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
                    "infoFiltered": "(Filtrado de _MAX_ total entradas)",
                    "infoPostFix": "",
                    "thousands": ",",
                    "lengthMenu": "Mostrar _MENU_ Entradas",
                    "loadingRecords": "Cargando...",
                    "processing": "Procesando...",
                    "search": "Buscar:",
                    "zeroRecords": "Sin resultados encontrados",
                    "paginate": {
                      "first": "Primero",
                      "last": "Ultimo",
                      "next": "Siguiente",
                      "previous": "Anterior"
                    },
                  },
            });
        },
        error: function(error){
            console.log(error);
        }
    });
}
function listadoPorcentajes(){
    $.ajax({
        url: "/institucion/promedio_asistencia_alumno/",
        type: "get",
        dataType: "json",
        success: function(response){
            if($.fn.DataTable.isDataTable('#tabla_porcentaje')){
                $('#tabla_porcentaje').DataTable().destroy();
            }
            $('#tabla_porcentaje tbody').html("");
            for(let i = 0;i < response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + (i+1) + '</td>';
                if (response[i]["fields"]['id_materia'] == ''){
                    fila += '<td> Desconocido </td>';
                } else {
                    fila += '<td>' + response[i]["fields"]['id_materia'] + '</td>';       
                }
                if (response[i]["fields"]['id_alumno'] == ''){
                    fila += '<td> Desconocido </td>';
                } else {
                    fila += '<td>' + response[i]["fields"]['id_alumno'] + '</td>';       
                }
                fila += '<td>' + response[i]["fields"]['promedio'] + '</td>';
                fila += '</tr>';
                $('#tabla_porcentaje tbody').append(fila);
            }             
            $('#tabla_porcentajes').DataTable({
                language: {
                    "decimal": "",
                    "emptyTable": "No hay información",
                    "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                    "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
                    "infoFiltered": "(Filtrado de _MAX_ total entradas)",
                    "infoPostFix": "",
                    "thousands": ",",
                    "lengthMenu": "Mostrar _MENU_ Entradas",
                    "loadingRecords": "Cargando...",
                    "processing": "Procesando...",
                    "search": "Buscar:",
                    "zeroRecords": "Sin resultados encontrados",
                    "paginate": {
                      "first": "Primero",
                      "last": "Ultimo",
                      "next": "Siguiente",
                      "previous": "Anterior"
                    },
                  },
            });
        },
        error: function(error){
            console.log(error);
        }
    });
}
function registrar() {
    activarBoton();
    var data = new FormData($('#form_creacion').get(0));
    $.ajax({        
        url: $('#form_creacion').attr('action'),
        type: $('#form_creacion').attr('method'), 
        data: data,
        cache: false,
        processData: false,
        contentType: false, 
        success: function (response) {
            notificacionSuccess(response.mensaje);
            listadoPorcentaje();
            cerrar_modal_creacion();
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresCreacion(error);
            activarBoton();
        }
    });
}
function editar() {
    activarBoton();
    var data = new FormData($('#form_edicion').get(0));
    $.ajax({        
        url: $('#form_edicion').attr('action'),
        type: $('#form_edicion').attr('method'), 
        data: data,
        cache: false,
        processData: false,
        contentType: false, 
        success: function (response) {
            notificacionSuccess(response.mensaje);
            listadoPorcentaje();
            cerrar_modal_edicion();
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresEdicion(error);
            activarBoton();
        },        
    });
}
function eliminar(pk){
	$.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
		url: '/institucion/materia/eliminar_materia/'+pk+'/',
		type: 'post',
		success: function(response) {
            notificacionSuccess(response.mensaje);
			listadoPorcentaje();
			cerrar_modal_eliminacion();
		},
		error: function(error) {
            notificacionError(error.responseJSON.mensaje);
		}
	});
}
$(document).ready(function(){
    listadoPorcentaje();
    listadoPorcentajes();
});