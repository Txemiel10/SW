package micarpeta;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class HolaMundoHTML
 */
@WebServlet("/HolaMundoHTML")
public class HolaMundoHTML extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public HolaMundoHTML() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		System.out.println("---> Entering HolaMundoHTML servlet GET");
		response.setContentType("text/html"); //
		PrintWriter out = response.getWriter();
		// Construimos una página HTML
		out.println("<HTML>");
		out.println("<HEAD><TITLE>Servlet simple que genera un HTML</TITLE></HEAD>");
		out.println("<BODY>");
		out.println("<H2>Servlet que genera un HTML</H2>");
		out.println("<P>Este Servlet devuelve el código de una página HTML que el");
		out.println(" navegador interpreta y muestra como tal.</P>");
		out.println("</BODY>");
		out.println("</HTML>");
		out.flush(); // fuerza la escritura de los datos
		out.close(); // cierra el fluj0
		System.out.println("<--- Exiting HolaMundoHTML servlet GET");
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
