import 'package:flutter/material.dart';
import 'consultaAPI.dart';
import 'package:http/http.dart' as http; // acesso web
import 'dart:convert'; // tratamento do JSON

void main() {
  runApp(const MaterialApp(
    home: Home(),
    debugShowCheckedModeBanner: false,
  ));
}

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  final GlobalKey<FormState> formKey = GlobalKey<FormState>();
  TextEditingController usuario = TextEditingController();
  TextEditingController senha = TextEditingController();

  //Método para enviar dados para outras telas (dados.dart)
  void enviarDadosOutraTelas(BuildContext context) {
    String cep = '', user = '', senha2 = ''; // Rua da Glória
    Map<String, dynamic> data = {}; // pessoa = {"nome": "Edson"}
    String errorMessage = '';
    Future<void> fetchData() async {
      print("TA Aqui");
      cep = '07807050';
      user = 'gus1234';
      senha2 = 'gus1234';

      // response vai conter os dados retornados da consulta externa
      try {
        // tratamento de erros
        final response = await http.post(
            Uri.parse('https://todolist-api.edsonmelo.com.br/api/user/login'),
            headers: {"Content-Type": "application/json"},
            body: jsonEncode({"username": user, "password": senha2}));
        print(response.body);
        if (response.statusCode == 200) {
          // deu bom
          print("Funcionou");
          setState(() {
            data = json.decode(response.body); // converte os dados recebidos
            errorMessage = '';
            print(data);
          });
        } else if (response.statusCode == 400) {
          // Lança um excessão que o servidor retornou algum erro
          throw Exception('CEP inválido');
        } else if (response.statusCode == 404) {
          throw Exception('CEP não encontrado');
        } else {
          throw Exception('Ocorreu um erro insperado.\nTente novamente.');
        }
        print(response.body);
      } catch (e) {
        print("Erro" + e.toString());
        // pega o erro e vamos tratar isso
        setState(() {
          data = {};
          // errorMessage =
          // 'Erro ao carregar os dados do CEP.\nPor favor, verifique o CEP e tente novamente.$e';
          errorMessage = '$e';
          errorMessage = errorMessage.replaceAll('Exception:', '');
        });
      }
      // Testando nosso código
      // print(data);
      // print(errorMessage);
    }

    fetchData();

    List textToSend = <String>[usuario.text, senha.text];

    //widget responsável por enviar os dados
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => Dados(text: textToSend),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Telas'),
        centerTitle: true,
      ),
      body: SingleChildScrollView(
        child: Form(
          key: formKey, //identificador do formulario
          child: Column(children: [
            Padding(
              padding: const EdgeInsets.only(top: 50),
              child: TextFormField(
                controller: usuario,
              ),
            ),
            Padding(
              padding: const EdgeInsets.only(top: 50),
              child: TextFormField(
                controller: senha,
              ),
            ),
            Padding(
              padding: const EdgeInsets.only(top: 50),
              child: SizedBox(
                height: 20,
                child: RawMaterialButton(
                  onPressed: () {
                    enviarDadosOutraTelas(context);
                  },
                  child: const Text('Login'),
                ),
              ),
            )
          ]),
        ),
      ),
    );
  }
}
