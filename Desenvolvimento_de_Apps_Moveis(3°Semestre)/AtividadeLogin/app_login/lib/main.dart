import 'package:flutter/material.dart';
import 'consultaAPI.dart';

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
