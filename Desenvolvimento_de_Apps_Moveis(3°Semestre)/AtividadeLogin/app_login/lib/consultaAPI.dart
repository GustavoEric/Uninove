import 'package:flutter/material.dart';

class Dados extends StatelessWidget {
  //variavel para receber os dados
  final List text;

  //no construtor pegar dados enviados
  const Dados({Key? key, required this.text}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Dados Enviados"),
      ),
      body: Center(
        child: Column(children: [
          Text(text[0], style: const TextStyle(fontSize: 24)),
          Text(text[1], style: const TextStyle(fontSize: 24)),
          MaterialButton(
            onPressed: () {
              Navigator.pop(context);
            },
            child: const Text('Voltar'),
          )
        ]),
      ),
    );
  }
}
