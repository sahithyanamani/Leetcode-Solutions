# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # ---------------------------------------------------------
        # 1️⃣ Brute Force
        # Collect all node values, sort them, and rebuild a linked list
        # ---------------------------------------------------------
        '''
        nodeval = []

        for lst in lists:
            while lst:
                nodeval.append(lst.val)
                lst = lst.next

        nodeval.sort()

        res = ListNode(0)
        curr = res

        for val in nodeval:
            curr.next = ListNode(val)
            curr = curr.next

        return res.next

        # ⏱ Time Complexity: O(N log N)
        # - N = total number of nodes across all lists
        #
        # 🧠 Space Complexity: O(N)
        # - store all values in array
        '''


        # ---------------------------------------------------------
        # 2️⃣ Min Heap
        # Always take the smallest current node among k lists
        # ---------------------------------------------------------
        heap = []

        # Push the first node of each list into the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
                # tuple used because:
                # 1️⃣ node.val → heap compares by smallest value
                # 2️⃣ i        → tie-breaker if values are equal
                # 3️⃣ node     → actual node reference

        d = ListNode()   # ✅ dummy head for result list
        curr = d

        while heap:
            val, i, node = heapq.heappop(heap)
            # ✅ get smallest node among current heads

            curr.next = node
            curr = curr.next

            node = node.next
            # move to next node in that same list

            if node:
                heapq.heappush(heap, (node.val, i, node))
                # ✅ push next node from same list into heap

        return d.next


# ---------------------------------------------------------
# 🧩 Explanation:
# - Heap always stores the smallest available node
#   from each of the k linked lists.
# - Pop smallest node → attach to result
# - Push that node’s next pointer into heap
# - Continue until heap is empty
#
# This is more efficient than brute force because we do
# not sort all N elements at once.

# Example:
# lists = [[1,4,5],[1,3,4],[2,6]]
# heap pops in order:
# 1,1,2,3,4,4,5,6

# ---------------------------------------------------------
# ⏱ Time Complexity (Heap): O(N log k)
# - N = total number of nodes
# - k = number of linked lists
# - each push/pop from heap costs O(log k)

# 🧠 Space Complexity (Heap): O(k)
# - heap stores at most k nodes at a time
# - result reuses existing nodes
# ---------------------------------------------------------
