//java program to connect to the azure database and get branch branch details`


import java.sql.*;
import java.util.*;
import java.util.logging.Logger;

public class azureFetchRecord {

  private static void insertData(Connection connection) throws SQLException {
  log.info("Insert data");
  PreparedStatement insertStatement = connection
          .prepareStatement("INSERT INTO branch (address, bank, ifsc) VALUES (?, ?, ?);");

  Scanner s = new Scanner(System.in);
  System.out.println("Enter Bank Name: ");
  String name = s.nextLine();
  System.out.println("Enter IFSC: ");
  String ifsc = s.nextLine();
  System.out.println("Enter Address: ");
  String add = s.nextLine();

  insertStatement.setString(1, add);
  insertStatement.setString(2, name);
  insertStatement.setString(3, ifsc);
  insertStatement.executeUpdate();
  return;
}
  private static void readData(Connection connection) throws SQLException {
  log.info("Read data");
  /*
  PreparedStatement readStatement = connection.prepareStatement("SELECT * FROM branch;");
  ResultSet resultSet = readStatement.executeQuery();
  */
  Scanner s = new Scanner(System.in);
  System.out.println("Enter Bank Name or IFSC: ");
  String name = s.nextLine();
  String query1 = "SELECT * FROM branch WHERE bank = ?;";
  PreparedStatement readStatement = connection.prepareStatement(query1);
  //statement.setQueryTimeout(40); //timeout of 40 seconds
  //String query, startquery="", condition="", endquery="";
  //query = startquery + condition + endquery;
  //PreparedStatement readStatement = connection.prepareStatement("SELECT * FROM branch;");
  readStatement.setString(1, name);
  //ResultSet resultSet = readStatement.executeQuery();
  ResultSet rs1 = readStatement.executeQuery();
  while(rs1.next())
  {
    //read the output
    System.out.print("BANK: "+rs1.getString("bank"));
    System.out.print("IFSC: "+rs1.getString("ifsc"));
    System.out.print("ADDRESS: "+rs1.getString("address")+"\n");
  }


    String query2 = "SELECT * FROM branch WHERE ifsc = ?;";
    readStatement = connection.prepareStatement(query2);
    readStatement.setString(1, name);
  ResultSet rs2 = readStatement.executeQuery();
  while(rs2.next())
  {
    //read the output
    System.out.print("BANK: "+rs2.getString("bank"));
    System.out.print("IFSC: "+rs2.getString("ifsc"));
    System.out.print("ADDRESS: "+rs2.getString("address")+"\n");
  }

  log.info("Data read from the database");
  return;
}

private static final Logger log;

static {
    System.setProperty("java.util.logging.SimpleFormatter.format", "[%4$-7s] %5$s %n");
    log =Logger.getLogger(azureConnect.class.getName());
}
    public static void main(String[] args) throws Exception {
        log.info("Loading application properties");
        Properties properties = new Properties();
        properties.load(azureBranch.class.getClassLoader().getResourceAsStream("application.properties"));

        log.info("Connecting to the database");
        Connection connection = DriverManager.getConnection(properties.getProperty("url"), properties);
        log.info("Database connection test: " + connection.getCatalog());

        /*
        log.info("Create database schema");
        Scanner scanner = new Scanner(DemoApplication.class.getClassLoader().getResourceAsStream("schema.sql"));
        Statement statement = connection.createStatement();
        while (scanner.hasNextLine()) {
            statement.execute(scanner.nextLine());
        */



		    azureBranch obj = new azureBranch();
        //obj.insertData(connection);
        obj.readData(connection);
      //  obj.updateData(todo, connection);
      //  obj.deleteData(todo, connection);


        log.info("Closing database connection");
        connection.close();
      }
}
