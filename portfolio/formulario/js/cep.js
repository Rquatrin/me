function buscarEndereco(){
    var cep = $('#cep').val().replace('.','');
    $.ajax({
        type: 'GET',
        url:`https://viacep.com.br/ws/${cep}/json/`,
        timeout: 2000, //timeout para esperar 2 segundos pela resposta de requisição
        success: function(data){
            if(data.localidade){
                $('#cidade').val(data.localidade);
                $('#uf').val(data.uf);
                $('#bairro').val(data.bairro); 
                $('#logradouro').val(data.logradouro);
                $('#numero').val(data.numero);
            }else{
                alert("Cep inválido");
            }
        },
        error: function(){
            alert('Não foi possível retornar a busca')
        }
    });
}