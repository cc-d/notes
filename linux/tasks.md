Both threads and processes are represented by `task_struct`.

Processes are self-contained in regards to memory space, file descriptors, ... and are created by the `fork()` system call.


Threads share the parent processes memory spaces, ... but have their own stack. Created by the `clone()` system call.

Scheduler ensures that each task/thread are executed appropriately.

Memory:
	
	Virtual:
		
	
	Physical

	The Memory Management Unit is a hardware component that translates virtual addresses to physical addresses, using page tables.

        Paging allows kernent to present contiguous address space to each process, regardless of the physical RAM structure, these blocks are called pages.
	
	Page tables - the mapping of physical to virtual addresses. Specifically virtual address blocks to physical frames.

Queues:
	Run - Each cpu core has its own run queue, containing tasks waiting o be executed by the scheduler.
	IO - the I/O scheduler manages I/O operations using an I/O queue and I/O scheduler.

	Wait - manages tasks that are waiting for completion of an operation or a resource to be avaliable. When waited, a task is put on this queue and put to sleep, and is moved back to the run queue whenever the waited event occurs.





Filesystems - linux uses the Virtual File System VFS layer to provide a generalized interface across different filesystems.

	Virtual filesystems:
		procfs - processes, sockets, etc
		sys - hardware devices and attributes
		tmpfs - in-memory temporary filesystem

Registers - small extremely performant storage locations within the cpu, managed by the kernel directly in regards to program execution. When switching between tasks, cpu register state is saved and the next task's registers are loaded.
	
	Some examples of the data stored in registers are:
	Instruction Pointer (IP): memory address of next cpu instruction
	Stack Pointer (SP) - top of current task's stack
	The Control Registers - control aspects cpu operation, IE physical base address ofpage table for current process, ...
	Floating-Point - specifalized registers for specifically floating-point math.
	RFLAGS Register - status flags and control flags	


