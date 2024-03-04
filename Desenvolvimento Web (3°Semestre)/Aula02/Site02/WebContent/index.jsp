<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
	<!--Enviando os dados para a pagina salvar.jsp com o metodo POST-->
	<form action="salvar.jsp" method="post" >
		<input type="text" name="txtname" placeholder="Nome:">
        <input type="text" name="txtra" placeholder="RA:">
        <button type="submit">Enviar</button>
	</form>
	<form action ="https://www.google.com/search" method="get">
		<input type="text" name="q" placeholder="Buscar">
		<button type="submit">Pesquisar</button>
	</form>
</body>
</html>