<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
	<%
	    //Pegando os dados da pagina indes.jsp
		String nome = request.getParameter("txtname");
		out.print("Nome: "+nome);
		String ra = request.getParameter("txtra");
		out.print("\nRa: "+ra);
	%>
</body>
</html>