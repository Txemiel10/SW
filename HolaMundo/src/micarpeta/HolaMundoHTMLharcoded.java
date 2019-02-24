package micarpeta;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


/**
 * Servlet implementation class HolaMundoHTMLharcoded
 */
@WebServlet("/HolaMundoHTMLharcoded")
public class HolaMundoHTMLharcoded extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public HolaMundoHTMLharcoded() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("---> Entering HolaMundoHTMLDispatched servlet GET");
		response.setContentType("text/html");
		System.out.println(" Redirecting to HTML document");
		RequestDispatcher rd = request.getRequestDispatcher("/html/DoGetDoPost.html");
		rd.forward(request, response);
		System.out.println("<--- Exiting HolaMundoHTMLDispatched servlet GET");
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
