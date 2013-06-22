#pragma once
// DynamicArray.h

#include "CvDLLEntity.h"
#include "CvGlobals.h"

/*
 * Guide for just-in-time array usage
 *  This is classes containing a single pointer. This means from a coding point of view they can be used like an array.
 *  The main difference from normal arrays is that they will not allocate memory until a non-default value is written in it.
 *  This is useful for arrays where say only human players will use them. AI players will then not allocate the memory at all.
 *  The length of the array is hardcoded into the class, eliminating the risk of assuming wrong length.
 *
 *  Usage:
 *   get() reads data from array. 0 or false is returned when read from an unallocated array.
 *   set() writes data to array. Allocates if needed.
 *   hasContent() and isEmpty() tells if the array is allocated.
 *     They also frees the array if it only contains 0/false.
 *   IsAllocated() returns true if the array is allocated but doesn't check contents (faster than hasContent())
 *   read()/write() used for savegames. The bool tells if the data should be read/written.
 *      This allows one-line statements when saving, which includes the if sentence.
 *   reset() frees the array
 *
 *  Adding new types:
 *   As complex as it may look, adding a new type is easy.
 *   Copy class YieldArray, call it something else and change length.
 *
 *  The reason why the class function definitions are inside the declaration is to avoid compiler errors regarding templates.
 */

template<class T> class JustInTimeArray
{
private:
	T* tArray;

public:
	JustInTimeArray()
	{
		tArray = NULL;
	}

	~JustInTimeArray()
	{
		SAFE_DELETE_ARRAY(tArray);
	}

	void reset()
	{
		SAFE_DELETE_ARRAY(tArray);
	}

	inline bool isAllocated() const
	{
		return tArray != NULL;
	}

	// used when constructor isn't called, like in an array
	inline void init()
	{
		tArray = NULL;
	}

protected:
	inline T zParentGet(int iLength, int iIndex) const
	{
		FAssert(iIndex >= 0);
		FAssert(iIndex < iLength);
		return tArray ? tArray[iIndex] : 0;
	}

	inline void zParentSet(int iLength, T value, int iIndex)
	{
		FAssert(iIndex >= 0);
		FAssert(iIndex < iLength);

		if (tArray == NULL)
		{
			if (value == 0)
			{
				// no need to allocate memory to assign a default (false) value
				return;
			}
			tArray = new T[iLength];
			for (int iIterator = 0; iIterator < iLength; ++iIterator)
			{
				tArray[iIterator] = 0;
			}
		}
		tArray[iIndex] = value;
	}

	bool zParentHasContent(int iLength, bool bRelease)
	{
		if (tArray == NULL)
		{
			return false;
		}
		for (int iIterator = 0; iIterator < iLength; ++iIterator)
		{
			if (tArray[iIterator])
			{
				return true;
			}
		}

		if (bRelease)
		{
			// array is allocated but has no content
			SAFE_DELETE_ARRAY(tArray);
		}
		return false;
	};
	inline bool zParentIsEmpty(int iLength, bool bRelease)
	{
		return !ParentHasContent(iLength, bRelease);
	}

	void zParentRead( int iLength, FDataStreamBase* pStream, bool bRead)
	{
		if (bRead)
		{
			if (tArray == NULL)
			{
				tArray = new T[iLength];
			}
			pStream->Read(iLength, tArray);
		}
	}

	void zParentWrite(int iLength, FDataStreamBase* pStream, bool bWrite)
	{
		if (bWrite)
		{
			FAssert(tArray != NULL);
			pStream->Write(iLength, tArray);
		}
	}
};


template<class T>
class YieldArray: public JustInTimeArray<T>
{
public:
	enum {length = NUM_YIELD_TYPES};

	inline T get(int iIndex) const             {return zParentGet(length, iIndex);}
	inline void set(T value, int iIndex)       {zParentSet(length, value, iIndex);}
	inline bool hasContent(bool bRelease = true)              {return zParentHasContent(length, bRelease);}
	inline bool isEmpty(bool bRelease = true)                 {return !zParentHasContent(length, bRelease);}
	inline void read(FDataStreamBase* pStream, bool bRead)    {zParentRead(length, pStream, bRead);}
	inline void write(FDataStreamBase* pStream, bool bWrite)  {zParentWrite(length, pStream, bWrite);}
};

template<class T>
class UnitArray: public JustInTimeArray<T>
{
public:
	int length;

	UnitArray()
	{
		length = GC.getNumUnitInfos();
		FAssertMsg(length > 0, "Array length is set before XML is read")
	}

	inline T get(int iIndex) const                            {return zParentGet(length, iIndex);}
	inline void set(T value, int iIndex)                      {zParentSet(length, value, iIndex);}
	inline bool hasContent(bool bRelease = true)              {return zParentHasContent(length, bRelease);}
	inline bool isEmpty(bool bRelease = true)                 {return !zParentHasContent(length, bRelease);}
	inline void read(FDataStreamBase* pStream, bool bRead)    {zParentRead(length, pStream, bRead);}
	inline void write(FDataStreamBase* pStream, bool bWrite)  {zParentWrite(length, pStream, bWrite);}
};