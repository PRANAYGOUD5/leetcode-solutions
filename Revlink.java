
class Revlink {
    public ListNode reverseList(ListNode head) {
        ListNode temp=head;
        ListNode prev=null;
        ListNode front;
        if (head==null || head.next==null){
            return head;
        }
        while(temp!=null){
            front=temp.next;
            temp.next=prev;    
            prev=temp;
            temp=front;
        }
    return prev;
    }
}
