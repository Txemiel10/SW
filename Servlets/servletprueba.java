package pruebaBD;


import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import java.sql.*;

/**
 * Servlet implementation class main_db
 */
@WebServlet("/main_db")
public class PruebaBD extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public PruebaBD() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		String url = "jdbc:mysql://localhost/";
	    String db = "test";
	    String user = "root"; 
	    String passwd = "luz2015";
		String driver = "com.mysql.jdbc.Driver";
			
		
	    Connection conn = null;
	    ResultSet res = null;

	    PrintWriter http_out = response.getWriter();
	    try {
	        Class.forName(driver).newInstance();
	        conn = DriverManager.getConnection(url+db,user,passwd);
	        http_out.println("Database connection successfully established!");
	       
	        
        	String query = "SELECT * FROM logindata;"; 
	        Statement st = conn.createStatement();
	        res = st.executeQuery(query);
	        http_out.println("Database query: " + query);
	        
    	   	
	        while(res.next()) {
	        	http_out.println("Database results: " + res.getString("id") + ", " + res.getString("passwd"));
	        }
        } catch(Exception e) {
        	System.out.println("Exception: " + e.getMessage());
    	}
	    http_out.flush();
	    http_out.close();
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}