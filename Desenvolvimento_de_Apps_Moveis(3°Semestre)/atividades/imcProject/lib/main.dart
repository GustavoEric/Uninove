// ignore_for_file: library_private_types_in_public_api

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

void main() {
  runApp(const MaterialApp(
    home: Home(), // primeira tela do aplicativo (rota)
    debugShowCheckedModeBanner: false, // tira o logo do debug
  ));
}

class Home extends StatefulWidget {
  const Home({super.key});
  @override // sobrescrita de método da classe pai
  // criação de um controle de estado para a aplicação
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  // definição dos objetos (controladores ou controllers)
  // TextEditingController: campo de entrada de dados texto (input)
  TextEditingController alturaController = TextEditingController();
  TextEditingController pesoController = TextEditingController();
  String _resultado = ''; // texto de resposta da aplicação

  // objeto para controlar o fomulário onde estarão os inputs
  GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  // método que altera o "estado" das variáveis
  // limpa os campos do formulário e o seu estado
  void _reset() {
    setState(() {
      alturaController.text = '';
      pesoController.text = '';
      _resultado = '';
      _formKey = GlobalKey<FormState>();
    });
  }

  // realiza o cálculo dos valores dos combustíveis
  // não pode esquecer de usar o setState() dentro de um
  // método que fará alguma alteração em variáveis e/ou objetos
  void _calcularIMC() {
    double varPeso = double.parse(pesoController.text.replaceAll(',', '.'));
    double varAltura = double.parse(alturaController.text.replaceAll(',', '.'));
    double imc = varPeso / (varAltura * varAltura);
    setState(() {
      // abaixo está sendo usado um operador ternário (substitui o if-else)
      if (imc < 18.5) {
        _resultado = 'IMC: ' + imc.toStringAsFixed(2) + ' Abaixo do peso';
      } else if (imc > 18 && imc <= 24.9) {
        _resultado = 'IMC: ' + imc.toStringAsFixed(2) + ' Peso normal';
      } else if (imc > 24.9 && imc <= 29.9) {
        _resultado = 'IMC: ' + imc.toStringAsFixed(2) + ' Sobrepeso';
      } else if (imc > 29.9 && imc <= 34.9) {
        _resultado = 'IMC: ' + imc.toStringAsFixed(2) + ' Obesidade grau I';
      } else if (imc > 34.9 && imc <= 39.9) {
        _resultado = 'IMC: ' + imc.toStringAsFixed(2) + ' Obesidade grau II';
      } else if (imc > 39.9) {
        _resultado = 'IMC: ' + imc.toStringAsFixed(2) + ' Obesidade grau III';
      }
    });
  }

  // construtor que implementa a interface do usuário
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // barra superior
      appBar: AppBar(
        title: const Text(
          'Calculadora IMC',
          style: TextStyle(color: Colors.white),
        ),
        centerTitle: true,
        backgroundColor: Colors.lightBlue[900],
        actions: <Widget>[
          IconButton(
              onPressed: () {
                _reset();
              },
              icon: const Icon(Icons.refresh, color: Colors.white)),
        ],
      ),
      // vamos montar o corpo da aplicação
      body: SingleChildScrollView(
        padding: const EdgeInsets.fromLTRB(15.0, 0, 15.0, 0), // margem interna
        child: Form(
          key: _formKey, // é a referência para o formulário
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch, // alargar
            // aqui vamos colocar os campos de entrada (inputs)
            children: <Widget>[
              const Icon(
                Icons.balance,
                size: 70.0,
                color: Colors.black,
              ),
              TextFormField(
                controller: alturaController,
                textAlign: TextAlign.center,
                keyboardType: TextInputType.number,
                validator: (value) =>
                    value!.isEmpty ? 'Esse valor é Obrigatório' : null,
                decoration: InputDecoration(
                  labelText: 'Qual a sua altura',
                  labelStyle: TextStyle(color: Colors.lightBlue[900]),
                ),
                style: TextStyle(color: Colors.lightBlue[900], fontSize: 25.0),
              ),
              TextFormField(
                controller: pesoController,
                textAlign: TextAlign.center,
                keyboardType: TextInputType.number,
                validator: (value) =>
                    value!.isEmpty ? 'Esse valor é Obrigatório' : null,
                decoration: InputDecoration(
                  labelText: 'Digite seu peso:',
                  labelStyle: TextStyle(color: Colors.lightBlue[900]),
                ),
                style: TextStyle(color: Colors.lightBlue[900], fontSize: 25.0),
              ),
              Padding(
                padding: const EdgeInsets.only(top: 50.0, bottom: 50.0),
                child: SizedBox(
                  height: 50,
                  child: RawMaterialButton(
                    onPressed: () {
                      if (_formKey.currentState!.validate()) {
                        _calcularIMC();
                      }
                    },
                    fillColor: Colors.lightBlue,
                    child: const Text(
                      'Calcular',
                      style: TextStyle(color: Colors.white, fontSize: 25.0),
                    ),
                  ),
                ),
              ),
              Text(
                _resultado, //Variavel com o valor do resultado Retornado
                textAlign: TextAlign.center,
                style: TextStyle(color: Colors.lightBlue, fontSize: 25.0),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
