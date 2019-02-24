package micarpeta;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class HolaMundoGetPost
 */
@WebServlet("/HolaMundoGetPost")
public class HolaMundoGetPost extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public HolaMundoGetPost() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("---> Entering HolaMundoGetPost servlet GET");
		String nombre = request.getParameter("nombre");
		PrintWriter out = response.getWriter();
		try {
		out.println("Hola, " + nombre);
		out.println("Has pasado tu nombre con GET en la URI.");
		} finally {
		out.close();
		}
		System.out.println("<--- Exiting HolaMundoGetPost servlet GET");
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("---> Entering HolaMundoGetPost servlet GET");
		String nombre = request.getParameter("nombre");
		PrintWriter out = response.getWriter();
		try {
		out.println("Hola, " + nombre);
		out.println("Has pasado tu nombre con POST en el cuerpo de la petición");
		} finally {
		out.close();
		}
		System.out.println("<--- Exiting HolaMundoGetPost servlet GET");
	}

}
