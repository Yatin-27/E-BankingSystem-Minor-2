/*import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.DriverManager;*/
import java.util.*;
import java.sql.*;
class BranchDetails{

  String bank;
  String ifsc;
  String address;

  void addBranch(String bank, String ifsc, String address){

    if(bank.length()<1 || ifsc.length()<1 || address.length()<1){
      System.out.println("NO INPUT!!!\nRecord Not Added");
      return;
    }
    String query = "INSERT INTO branch(ifsc, bank, address) VALUES (?, ?, ?);";
    System.out.println("Adding Record...");
    try(Connection con = DriverManager.getConnection("jdbc:sqlite:bankDB.sqlite");
    PreparedStatement pstmt = con.prepareStatement(query);){
      //database Connection
        pstmt.setString(1, ifsc);
        pstmt.setString(2, bank);
        pstmt.setString(3, address);
        pstmt.executeUpdate();
        System.out.println("Added "+ ifsc);
        con.close();
      }

    catch(SQLException e){
      System.out.println("ERROR: "+ e.getMessage());

    }
    return;

  }

  void getBranch(String s){
    // s can be bank, ifsc
    //database Connection
    Connection c = null;
    try{
      //database connection
      c = DriverManager.getConnection("jdbc:sqlite:bankDB.sqlite");
      Statement statement = c.createStatement();
      statement.setQueryTimeout(40); //timeout of 40 seconds
      //String query, startquery="", condition="", endquery="";
      //query = startquery + condition + endquery;
      String query1 = "SELECT * FROM branch WHERE bank = \""+s+"\";";
      ResultSet rs1 = statement.executeQuery(query1);
      while(rs1.next())
      {
        //read the output
        System.out.print("BANK: "+rs1.getString("bank"));
        System.out.print("IFSC: "+rs1.getString("ifsc"));
        System.out.print("ADDRESS: "+rs1.getString("address")+"\n");
      }

      String query2 = "SELECT * FROM branch WHERE ifsc = \""+s+"\";";
      ResultSet rs2 = statement.executeQuery(query2);
      while(rs2.next())
      {
        //read the output
        System.out.print("BANK: "+rs2.getString("bank"));
        System.out.print("IFSC: "+rs2.getString("ifsc"));
        System.out.print("ADDRESS: "+rs2.getString("address")+"\n");
      }

    }
    catch(Exception e)
    {
      System.err.println(e.getMessage());
    }
    finally{
      try{
        if(c!=null)
          c.close();
        }
    catch(Exception e){
      System.err.println(e.getMessage());
    }
    }
  }

  void showallBranch(){
    Connection c = null;
    try{
      //database connection
          c = DriverManager.getConnection("jdbc:sqlite:bankDB.sqlite");
          Statement statement = c.createStatement();
          statement.setQueryTimeout(40); //timeout of 40 seconds
          //String query, startquery="", condition="", endquery="";
          //query = startquery + condition + endquery;
          String query1 = "SELECT * FROM branch;";
          ResultSet rs1 = statement.executeQuery(query1);
          while(rs1.next())
          {
            //read the output
            System.out.print("BANK: "+rs1.getString("bank")+"||\t ");
            System.out.print("IFSC: "+rs1.getString("ifsc")+"||\t ");
            System.out.print("ADDRESS: "+rs1.getString("address")+"\n");
          }
    }
    catch(Exception e){
      System.out.println("ERROR: "+e.getMessage());
    }
    finally{
      try{
        if(c!=null)
          c.close();
        }
    catch(Exception e){
      System.err.println(e.getMessage());
    }
    }
  }

  void deleteBranch(String bank, String ifsc){
    if(bank.length()<1||ifsc.length()<1){
      System.out.println("NO INPUT!!!\nRecord Not Deleted");
      return;
    }
    Connection c = null;
    try{
      //database connection
      c = DriverManager.getConnection("jdbc:sqlite:bankDB.sqlite");
      Statement statement = c.createStatement();
      statement.setQueryTimeout(40); //timeout of 40 seconds
      //String query, startquery="", condition="", endquery="";
      //query = startquery + condition + endquery;
      String query1 = "SELECT * FROM branch WHERE bank = \""+bank+"\" AND ifsc = \""+ifsc+"\";";
      ResultSet rs1 = statement.executeQuery(query1);
      if(rs1.next()){
        //record Exist
                try (Connection conn = DriverManager.getConnection("jdbc:sqlite:bankDB.sqlite");
                       PreparedStatement pstmt = conn.prepareStatement("DELETE FROM branch WHERE bank = ? AND ifsc = ?;")) {

                   // set the corresponding param
                   pstmt.setString(1, bank);
                   pstmt.setString(2, ifsc);
                   // execute the delete statement
                   pstmt.executeUpdate();
                   System.out.println("Branch Deleted: "+ifsc);
                   conn.close();

               } catch (SQLException e) {
                   System.out.println(e.getMessage());

               }



      }
      else{
        System.out.println("No match found!!!\n Bank and IFSC or both might be wrong");

      }

    }

    catch(SQLException e){
      System.out.println("ERROR: "+ e.getMessage());

    }
    finally{
      try{
        if(c!=null)
          c.close();
        }
    catch(Exception e){
      System.err.println(e.getMessage());
    }
    }

    return;

  }
  }

public class Connect
{
  public static void main(String[] args)
  {
    System.out.println("Minor 2 Project");
    char choice;
    System.out.println("");
    Scanner input = new Scanner(System.in);
    while(true){
        System.out.println("Enter 'A' to Add branch Enter 'D' to Delete, 'S' to show all branch, 'G' Get details of branch");
        choice = input.next().charAt(0);
        BranchDetails b = new BranchDetails();
        if(choice == 'A'|| choice =='a'){// add branch

          System.out.println("ADD BRANCH");
           System.out.println("Enter Bank, IFSC, Address: ");
             String bankName = input.nextLine();
             String ifsc =input.nextLine();
             String address = input.nextLine();
               b.addBranch(bankName, ifsc, address);
            }
        else if(choice == 'G'|| choice =='g'){// get specific branch
        System.out.println("GET BRANCH");
         System.out.println("Enter IFSC or BANK: ");
         input.nextLine();
           String s = input.nextLine();
             b.getBranch(s);
           }
        else if(choice == 'D'|| choice =='d')
      {//delete branch
            System.out.println("DELETE BRANCH");
            System.out.println("Enter Bank And IFSC: ");
            String bank = input.nextLine();
            String ifsc= input.nextLine();
             b.deleteBranch(bank, ifsc);
           }
    else if(choice == 'S' || choice =='s')
        {//show all Branch
            b.showallBranch();
            }

      else if(choice == ' '){
        System.out.println("Exiting!!");
        input.close();
        System.exit(0);
      }
      else{
        System.out.println("Exiting!!");
        input.close();
        System.exit(0);
      }
    }

}
}
