var itensOrcamento = []; //para resetar a lista, é essa varivável que irei "zerar"

function adicionarItem(){
    /*captura de elementos de input*/
    var inputDescricao = document.getElementById('descricao');
    var inputValor = document.getElementById('valor');

    //validar dados de entrada
    if(inputDescricao.value == '' || inputValor.value == ''){
        alert('Ops! Você deve preencher a descrição e o valor')
        return; /*o return faz a operação parar*/
    }

    /*console.log('Continua processando...');*/ //uso pra ver se tá funcionando via console

    //Monta um novo item no formato json
    var novoItem = {
        'descricao' : inputDescricao.value,
        'valor' : inputValor.value
    }

    //Adiciona um novo item no array de itens do orçamento

    itensOrcamento.push(novoItem);

    redesenharTabela();

    //limpar os campos de entrada

    inputDescricao.value = null;
    inputValor.value = null;
}

function redesenharTabela(){
    var corpoTabelaItens = ''; //variável que irá armazenar a lista em forma de um longo texto
    var somatorio = 0; //o somatório é a variável acumulatória
    
    for(var i = 0; i < itensOrcamento.length; i++){
        var item = itensOrcamento[i];
        var valor = parseFloat(item['valor']);

        somatorio += valor; //aqui é o somatório da lista, mais o valor novo

        corpoTabelaItens += `
            <tr>
                <td>${item['descricao']}</td>
                <td class="text-right">R$ ${valor.toFixed(2)}</td>
            </tr>
        `
    }

    var tabelasItensOrcamento = document.getElementById('tabela_itens_orcamento');
    tabelasItensOrcamento.innerHTML = corpoTabelaItens;

    var inputSomatorio = document.getElementById('somatorio');
    inputSomatorio.value = somatorio.toFixed(2);
    
}