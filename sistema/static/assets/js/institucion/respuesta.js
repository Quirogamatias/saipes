function listadoRespuesta(){
    $.ajax({
        url: "/institucion/listar_preguntas_alumno/",
        type: "get",
        dataType: "json",
        success: function(response){
            if($.fn.DataTable.isDataTable('#tabla_respuestas')){
                $('#tabla_respuestas').DataTable().destroy();
            }
            $('#tabla_respuestas tbody').html("");
            for(let i = 0;i < response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + (i+1) + '</td>';                
                if (response[i]["fields"]['id_pregunta'] == ''){
                    fila += '<td> Desconocido </td>';
                } else {
                    fila += '<td>' + response[i]["fields"]['id_pregunta'] + '</td>';       
                } 
                fila += '<td>' + response[i]["fields"]['contenido'] + '</td>';
                fila += '</tr>';
                $('#tabla_respuestas tbody').append(fila);
            }             
            $('#tabla_respuestas').DataTable({
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
function listadoRespuestasAdmin(){
    $.ajax({
        url: "/institucion/listar_respuestas/",
        type: "get",
        dataType: "json",
        success: function(response){
            if($.fn.DataTable.isDataTable('#tabla_respuestas_admin')){
                $('#tabla_respuestas_admin').DataTable().destroy();
            }
            $('#tabla_respuestas_admin tbody').html("");
            for(let i = 0;i < response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + (i+1) + '</td>';                
                if (response[i]["fields"]['id_pregunta'] == ''){
                    fila += '<td> Desconocido </td>';
                } else {
                    fila += '<td>' + response[i]["fields"]['id_pregunta'] + '</td>';       
                } 
                fila += '<td>' + response[i]["fields"]['contenido'] + '</td>';
                fila += '<td>' + response[i]["fields"]['mejor_respuesta'] + '</td>';
                fila += '<td> <button type = "button" class = "btn btn-primary btn-sm tableButton"';
                fila += ' onclick = "abrir_modal_edicion(\'/institucion/respuesta_editar/' + response[i]['pk']+'/\');"> EDITAR </button></td>';
                fila += '</tr>';
                $('#tabla_respuestas_admin tbody').append(fila);
            }             
            $('#tabla_respuestas_admin').DataTable({
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
            listadoRespuesta();
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
            listadoRespuestasAdmin();
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
		url: '/institucion/eliminar_horario/'+pk+'/',
		type: 'post',
		success: function(response) {
            notificacionSuccess(response.mensaje);
			listadoHorarios();
			cerrar_modal_eliminacion();
		},
		error: function(error) {
            notificacionError(error.responseJSON.mensaje);
		}
	});
}
$(document).ready(function(){
    listadoRespuesta();
    listadoRespuestasAdmin();
});