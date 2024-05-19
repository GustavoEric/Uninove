// ignore_for_file: library_private_types_in_public_api, depend_on_referenced_packages
import 'dart:io';

import 'package:http/http.dart' as http;
import 'dart:convert'; // tratamento do JSON
import 'package:flutter/material.dart'; // interface

// consulta de CEP
// doc: https://docs.awesomeapi.com.br/api-cep
// uri: https://cep.awesomeapi.com.br/{cep}
class Dados extends StatefulWidget {
  final List<dynamic> text;
  const Dados({Key? key, required this.text}) : super(key: key);

  @override
  _DadosPageState createState() => _DadosPageState();
}

class _DadosPageState extends State<Dados> {
  // lógica da aplicação
  String cep = ''; // Rua da Glória
  Map<String, dynamic> data = {}; // pessoa = {"nome": "Edson"}
  String errorMessage = '';

  // Construção do método para buscar os dados remotos na API
  // Endereço: https://cep.awesomeapi.com.br/{cep}
  //
  // Future: valor ou erro que estará disponível no futuro.
  // Usado em segundo plano para aguardar respostas remotas ou
  // que demandem espera.
  //
  // async: significa que a transação é "não sincronizada",
  // permitindo que outras coisas possam ser realizadas antes
  // que a resposta seja concluída.
  //
  // await: é usada para pausar uma execução de uma
  // função assíncrona até que um Future seja
  // resolvido (finalizado).
  //
  Future<void> fetchData(text) async {
    print("API");
    // response vai conter os dados retornados da consulta externa
    try {
      // tratamento de erros
      final response = await http.post(
          Uri.parse('https://todolist-api.edsonmelo.com.br/api/user/login'),
          headers: {"Content-Type": "application/json"},
          body: jsonEncode({
            "username": text[0],
            "password": text[1],
          }));
      if (response.statusCode == 200) {
        print("veio Aqui");
        // deu bom
        setState(() {
          data = json.decode(response.body); // converte os dados recebidos
          errorMessage = '';
        });
      } else if (response.statusCode == 400) {
        // Lança um excessão que o servidor retornou algum erro
        throw Exception('CEP inválido');
      } else if (response.statusCode == 404) {
        throw Exception('CEP não encontrado');
      } else {
        throw Exception('Ocorreu um erro insperado.\nTente novamente.');
      }
    } catch (e) {
      // pega o erro e vamos tratar isso
      data = {};
      // errorMessage =
      // 'Erro ao carregar os dados do CEP.\nPor favor, verifique o CEP e tente novamente.$e';
      errorMessage = '$e';
      errorMessage = errorMessage.replaceAll('Exception:', '');
    }
    // Testando nosso código
    // print(data);
    // pr
    // int(errorMessage);
  }

  // Se quisermos carregar qualquer coisa no início do APP
  // @override
  // void initState() {
  // super.initState();
  // fetchData(); // executa a consulta quando iniciar
  // }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('API CEP'),
      ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            const Text('Informe o CEP'),
            const SizedBox(height: 20),
            // Sem Controller
            TextField(
              onChanged: (value) {
                // muda conforme digita
                setState(() {
                  cep = value;
                });
              },
            ),
            // Botão para realizar a busca
            ElevatedButton(
              onPressed: () {
                fetchData(
                    widget.text[0]); // chama o método para buscar os dados
              },
              child: const Text('Buscar CEP'),
            ),
            // Tratamento dos erros ocorridos
            if (errorMessage.isNotEmpty)
              Text(errorMessage, style: const TextStyle(color: Colors.red)),

            // Ocultando os campos quando houver erro
            if (errorMessage.isEmpty && data.isNotEmpty)
              // Mostrando os dados retornados
              Text('Rua: ${data['name']}'),
          ],
        ),
      ),
    );
  }
}
