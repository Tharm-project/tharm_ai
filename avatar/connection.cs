using UnityEngine;
using System.Net;
using System.Net.Sockets;
using System.Text;

public class connection : MonoBehaviour
{
    private UdpClient udpClient;
    private const int port = 2000;

    void Start()
    {
        udpClient = new UdpClient(port);
        Debug.Log("UDP Server started on port " + port);
        ReceiveData();
    }

    private async void ReceiveData()
    {
        while (true)
        {
            UdpReceiveResult result = await udpClient.ReceiveAsync();
            string receivedMessage = Encoding.UTF8.GetString(result.Buffer);
            Debug.Log("Received message: " + receivedMessage);
        }
    }

    private void OnApplicationQuit()
    {
        udpClient.Close();
    }
}
